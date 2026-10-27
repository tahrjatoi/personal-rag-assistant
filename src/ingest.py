"""Document ingestion pipeline"""

import os
from pathlib import Path
from typing import List

def load_documents(data_dir: str = "data") -> List[str]:
    """Load all text/markdown files from data directory."""
    docs = []
    path = Path(data_dir)
    if not path.exists():
        path.mkdir(parents=True)
        print(f"Created {data_dir}/ — drop your documents there and re-run.")
        return docs
    
    for file in path.rglob("*"):
        if file.suffix.lower() in {".md", ".txt", ".markdown"}:
            try:
                content = file.read_text(encoding="utf-8")
                docs.append({"source": str(file), "content": content})
            except Exception as e:
                print(f"Skipping {file}: {e}")
    return docs

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100) -> List[str]:
    """Simple character-based chunking."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")
    for d in docs:
        chunks = chunk_text(d["content"])
        print(f"  {d['source']}: {len(chunks)} chunks")
