"""Simple chat loop over retrieved context"""

from retriever import SimpleRetriever
from ingest import load_documents, chunk_text

def build_context(retrieved: list) -> str:
    return "\n\n".join(
        f"Source: {d['source']}\n{d['content'][:500]}..." for d in retrieved
    )

def main():
    print("Personal RAG Assistant (demo mode)")
    print("Type 'quit' to exit.\n")
    
    docs = load_documents()
    if not docs:
        print("No documents found. Add files to the data/ folder first.")
        return
    
    # Flatten into chunks
    chunks = []
    for d in docs:
        for c in chunk_text(d["content"]):
            chunks.append({"source": d["source"], "content": c})
    
    retriever = SimpleRetriever()
    retriever.add_documents(chunks)
    
    while True:
        query = input("You: ").strip()
        if query.lower() in {"quit", "exit", "q"}:
            break
        
        results = retriever.search(query)
        if not results:
            print("Assistant: I couldn't find relevant information in your documents.\n")
            continue
        
        context = build_context(results)
        print("\nAssistant (using your documents):")
        print("(In full version this would be an LLM answer grounded in the context below)\n")
        print(context[:800] + "...\n")

if __name__ == "__main__":
    main()
