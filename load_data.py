"""
PharmGraph Data Ingestion Engine
Loads db_drug_interactions.csv into Neo4j Aura
Repository: https://github.com/omptra/pharmgraph-mcp
"""

import csv
import os
import re
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

URI      = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

BATCH_SIZE = 500


def parse_interaction(description: str):
    """Extract direction and effect type from description text."""
    match = re.search(
        r"may (increase|decrease|alter|inhibit|enhance|reduce|affect) the ([\w ]+? activities|[\w]+ rate|QTc)",
        description,
    )
    if match:
        direction = match.group(1)
        effect = re.sub(r" activities$", "", match.group(2)).strip()
        return direction, effect
    return None, None


def create_constraints(session):
    session.run("CREATE CONSTRAINT drug_name IF NOT EXISTS FOR (d:Drug) REQUIRE d.name IS UNIQUE")
    print("[PharmGraph] Constraints created.")


def load_interactions(session, rows):
    session.run(
        """
        UNWIND $rows AS row
        MERGE (d1:Drug {name: row.drug1})
        MERGE (d2:Drug {name: row.drug2})
        MERGE (d1)-[r:INTERACTS_WITH]->(d2)
        SET r.description = row.description,
            r.direction   = row.direction,
            r.effect      = row.effect
        """,
        rows=rows,
    )


def main():
    csv_path = os.path.join(os.path.dirname(__file__), "db_drug_interactions.csv")
    if not os.path.exists(csv_path):
        print(f"CSV not found at {csv_path}")
        return

    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

    with driver.session() as session:
        create_constraints(session)

        batch = []
        total = 0

        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                direction, effect = parse_interaction(row["Interaction Description"])
                batch.append({
                    "drug1":       row["Drug 1"].strip(),
                    "drug2":       row["Drug 2"].strip(),
                    "description": row["Interaction Description"].strip(),
                    "direction":   direction,
                    "effect":      effect,
                })

                if len(batch) >= BATCH_SIZE:
                    load_interactions(session, batch)
                    total += len(batch)
                    print(f"[PharmGraph] Loaded {total} interactions...")
                    batch = []

            if batch:
                load_interactions(session, batch)
                total += len(batch)

        print(f"\n[PharmGraph] Data Ingestion Complete! Total interactions loaded: {total}")

    driver.close()


if __name__ == "__main__":
    main()
