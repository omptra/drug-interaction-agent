# 💊 PharmGraph: Managed Graph Intelligence
### *An MCP-Native Knowledge Layer for AI-Native Pharmacological Reasoning*

PharmGraph is an intelligent pharmacological knowledge graph powered by the **Neo4j Aura Agent**. By mapping over **191,252 drug-drug interactions** across **1,701 generic drugs**, PharmGraph transforms raw data into a navigable "medical brain" that allows AI agents to reason over complex biochemical pathways natively.

---

## 🚀 The GraphRAG Advantage: Beyond Flat Data
Most medical RAG implementations treat documents as isolated chunks. PharmGraph treats pharmacology as an **interconnected web**, enabling insights that vector-only systems miss:

*   **⛓️ Multi-Hop Reasoning**: PharmGraph excels at discovering indirect interactions. It can answer: *"If Drug A inhibits Enzyme X, and Enzyme X is responsible for metabolizing Drug B, how does Drug A increase the risk of toxicity for Drug B?"*
*   **💥 The "Blast Radius" of Contraindications**: Just as security tools track vulnerability propagation, PharmGraph tracks how a single contraindication (like a liver enzyme deficiency) propagates across a patient's entire drug regimen.
*   **🛡️ Deterministic Grounding**: Unlike probabilistic LLMs, PharmGraph's answers are derived from explicit graph paths, eliminating hallucinations and providing a clear audit trail for clinical decisions.

---

## 🔌 Connecting to PharmGraph (MCP)
PharmGraph is an **MCP-native agent**. It can be added as a native tool to **Claude.ai** or **Claude Desktop** using our managed infrastructure:

> [!IMPORTANT]
> **Server Name**: `PharmGraph`  
> **MCP Endpoint**: `https://mcp.neo4j.io/agent?project_id=c095f5e2-d509-4db7-b848-8709ee7fcafc&agent_id=dc8e6f99-89b8-4099-9395-5e0af1d6aad0`  
> **Invoke API**: `https://api.neo4j.io/v2beta1/organizations/c095f5e2-d509-4db7-b848-8709ee7fcafc/projects/c095f5e2-d509-4db7-b848-8709ee7fcafc/agents/dc8e6f99-89b8-4099-9395-5e0af1d6aad0/invoke`

---

## 🧠 Managed Intelligence Toolset
Our Aura Agent leverages the **Neo4j Aura Agent** reasoning engine to orchestrate specialized tools:

1.  **Text2Cypher**: Dynamically translates natural language into precise graph traversals for ad-hoc exploration of unknown pathways.
2.  **Similarity Search**: Uses vector embeddings to find semantically related drugs or effects even when exact name matches fail.
3.  **Cypher Templates**: Pre-optimized logic for high-speed safety checks (e.g., cross-referencing a patient's drug list against a target contraindication).

---

## 📊 Ontology & Schema

| Element | Statistics |
| :--- | :--- |
| **Nodes** | 1,701 Drugs |
| **Relationships** | 191,252 Interactions |
| **Graph Stats** | 1.1M+ Properties |
| **Data Source** | DrugBank / Kaggle Pharmacological Dataset |

---

## ✨ What Makes PharmGraph Different?
1.  **AI-Native Architecture**: Built from the ground up for the Model Context Protocol, PharmGraph doesn't require a separate UI—it *becomes* a part of the LLM's reasoning process.
2.  **Clinical Grounding**: Every answer traces a relationship path. The agent never gives a lookup result without citing the specific graph path that produced it.
3.  **Scalability**: By utilizing Neo4j Aura, PharmGraph can handle millions of relationships with millisecond latency, outperforming traditional relational or vector-only databases in path-finding tasks.

---

## 🛠️ Developer Setup
If you wish to hydrate your own instance of this graph or explore the ingestion logic:

1.  **Clone this repo**:  
    `git clone https://github.com/omptra/pharmgraph-mcp`
2.  **Install requirements**:  
    `pip install -r requirements.txt`
3.  **Run ingestion**:  
    `python load_data.py` *(Ensure your `.env` is configured with Aura credentials)*

---

## 📂 Project Structure
```text
pharmgraph-mcp/
├── load_data.py        # Graph ingestion engine (Aura-optimized)
├── mcp-manifest.json   # Technical manifest for MCP integration
├── mcp_config.json     # Project metadata and endpoints
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## 💻 Tech Stack
- **Neo4j Aura Agent** — Managed reasoning & orchestration
- **Neo4j Aura Free** — Managed graph database
- **Model Context Protocol (MCP)** — Native AI integration
- **Neo4j Python Driver** — Data ingestion
- **Claude / Anthropic** — Recommended LLM for interaction

---

### *Built for the Neo4j Aura Agent Hackathon 2026*
**PharmGraph** — *Bridging the gap between raw data and AI-native pharmacological intelligence.*
