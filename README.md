# Personal RAG Assistant

Chat with your own notes, documents, and knowledge base using Retrieval-Augmented Generation.

This is a lightweight, developer-friendly RAG system you can run locally or point at any OpenAI-compatible API (including Grok).

## Why This Project?

Most people have scattered notes across Notion, Markdown files, PDFs, and chat history.  
This tool turns that mess into a searchable, conversational knowledge base.

Perfect for:
- Personal second brain
- Research paper collections
- Project documentation
- Learning notes

## Features

- Ingest Markdown, TXT, and PDF files
- Chunk + embed documents
- Query with natural language
- Source citations in answers
- Works with OpenAI, Grok, or local models (via Ollama)

## Quick Start

```bash
pip install -r requirements.txt
cp .env.example .env

# Add your documents
mkdir data
# drop .md / .txt / .pdf files into data/

# Ingest
python ingest.py

# Chat
python chat.py
```

## Project Structure

```
personal-rag-assistant/
├── data/               # Put your documents here
├── src/
│   ├── ingest.py       # Document loading & embedding
│   ├── retriever.py    # Vector search
│   └── chat.py         # Conversational interface
├── requirements.txt
└── .env.example
```

## Example

```
You: What did I decide about the RAG architecture last week?
Assistant: According to your notes from 2026-10-20, you decided to use ...
Sources: notes/rag-architecture.md
```

## Next Steps / Ideas to Extend

- Add web search as a fallback tool
- Support Notion / Google Drive sync
- Multi-user mode
- Streaming responses
- Evaluation harness for retrieval quality

---

Built by Tahir Jatoi · AI Engineer
