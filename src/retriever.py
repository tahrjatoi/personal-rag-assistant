"""Simple retriever (placeholder for vector store)"""

from typing import List, Dict

class SimpleRetriever:
    """
    Placeholder retriever.
    In a full implementation this would use Chroma / FAISS + embeddings.
    """
    def __init__(self):
        self.docs: List[Dict] = []
    
    def add_documents(self, documents: List[Dict]):
        self.docs.extend(documents)
    
    def search(self, query: str, k: int = 4) -> List[Dict]:
        """Naive keyword search for demo purposes."""
        query_terms = set(query.lower().split())
        scored = []
        for doc in self.docs:
            content_lower = doc["content"].lower()
            score = sum(1 for t in query_terms if t in content_lower)
            if score > 0:
                scored.append((score, doc))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for _, doc in scored[:k]]
