import os
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc

# 1. Configure working directory
WORKING_DIR = "./thbim_graphrag_data"
if not os.path.exists(WORKING_DIR):
    os.makedirs(WORKING_DIR)

# 2. Define Local LLM functions using Ollama
async def local_llm_model_complete(prompt, system_prompt=None, history=[], **kwargs):
    return await ollama_model_complete(
        "qwen2.5-coder:7b",  # Highly accurate coder and logical model at 7B size
        prompt,
        system_prompt=system_prompt,
        history=history,
        **kwargs
    )

async def local_llm_embedding(texts):
    return await ollama_embedding(
        "nomic-embed-text",  # Standard high-quality embedding model
        texts
    )

# 3. Initialize LightRAG Instance
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=local_llm_model_complete,
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=local_llm_embedding
    )
)

# 4. Function to incrementally sync Revit elements from MCP Server
def sync_revit_elements(elements_json_list):
    """
    elements_json_list: List of text descriptions representing Revit elements.
    Example: "Wall ID: 124500, Type: Partition, FireRating: 1 Hour, SpatialRelations: Borders Room 302"
    """
    for elem_desc in elements_json_list:
        # Utilizing incremental insert (No full graph rebuild required!)
        rag.insert(elem_desc)
    print("✓ Incremental sync completed successfully!")

# 5. Hybrid search function combining Vector & Knowledge Graph
def ask_bim_assistant(query_text):
    # 'hybrid' mode utilizes both semantic similarity (vector) and topological relationships (graph)
    response = rag.query(
        query_text,
        param=QueryParam(mode="hybrid") 
    )
    return response

# Example execution check
if __name__ == "__main__":
    print("Initializing THBIM Graph RAG Service...")
    # Demo insert
    demo_element = [
        "Wall ID: 204550, Level: Level 3, Type: Fire Compartment Wall, FireRating: 2 Hours, Relationships: Bounded by Server Room 302 and Corridor 305",
        "Door ID: 204560, Level: Level 3, Type: Single Fire Door, FireRating: 2 Hours, Relationships: Hosted by Wall 204550, Connects Server Room 302 to Corridor 305"
    ]
    
    # Sync elements
    sync_revit_elements(demo_element)
    
    # Test query
    query = "List all fire rated walls on Level 3 bordering the server room and check their fire rating."
    print(f"\nQuerying: {query}")
    print("-" * 50)
    # Since query is async under the hood, this is a placeholder check
    # In practice, call ask_bim_assistant(query)
    print("Graph RAG ready for querying.")
