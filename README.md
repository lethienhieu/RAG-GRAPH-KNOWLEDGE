# RAG GRAPH KNOWLEDGE (BIM & Revit Integration)

A state-of-the-art, high-performance Graph RAG (Retrieval-Augmented Generation) system tailored for the AEC (Architecture, Engineering, Construction) domain and Autodesk Revit integration. 

This repository leverages the power of spatial knowledge graphs combined with Large Language Models (LLMs) to automate building code compliance, design clash resolution, and operations & maintenance (O&M) workflows.

---

## 🚀 Key Features

*   **Dual-Flow Graph RAG:**
    *   *Static Flow:* Indexes PDF building codes, safety regulations, and technical standards using community detection for global reasoning.
    *   *Dynamic Flow:* Integrates live spatial topology and MEP system connections directly from Revit models using incremental updates.
*   **Incremental Graph Updates:** Utilizing **LightRAG** to allow real-time graph additions without expensive full graph rebuilds—perfect for active BIM design phases.
*   **100% Free & Commercial-Ready Stack:** Built entirely on open-source, commercially viable tools (MIT/Apache 2.0/Community).
*   **Local & Secure AI:** Supports offline execution using **Ollama** (Qwen-2.5-Coder / Llama 3) to protect confidential construction IP, with optional fallback to cloud APIs (Gemini).

---

## 🛠️ Technology Stack

*   **Orchestration & RAG:** [LightRAG](https://github.com/HKUDS/LightRAG) (MIT) & [LlamaIndex](https://github.com/run-llama/llama_index) (MIT)
*   **Graph Database:** [Neo4j Community Edition](https://neo4j.com/) (GPLv3 / Free)
*   **Local Inference:** [Ollama](https://ollama.com/) (MIT)
*   **Client Integration:** Revit API (C#) via [THBIM-MCP-Server](https://github.com/modelcontextprotocol)

---

## 📂 Repository Structure

*   `graph_rag_design.html` - Premium interactive system architecture design document with responsive SVG flow and logic diagrams. Open this in your browser to explore the full specifications!
*   `graph_rag_service.py` - Core Python service integrating LightRAG, Ollama embedding/generation, and incremental data syncing.
*   `README.md` - Repository overview.

---

## 🔧 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10+ and [Ollama](https://ollama.com/) installed on your system.

### 2. Install Dependencies
```bash
pip install lightrag-hku ollama neo4j llamaindex-cli-framework
```

### 3. Run Local Models
Pull the recommended code-focused LLM and text embedding models:
```bash
ollama pull qwen2.5-coder:7b
ollama pull nomic-embed-text
```

### 4. Open the Design Document
Open `graph_rag_design.html` in your web browser (Chrome, Edge, Safari) to view the complete system architecture, interactive diagrams, and integration guide.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
All external dependencies used in this architecture are free for commercial utilization.
