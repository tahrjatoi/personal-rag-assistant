<div align="center">

# Personal RAG Assistant

**Chat with your own notes, documents, and knowledge base using Retrieval-Augmented Generation.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## Overview

Most people have scattered knowledge across Notion, Markdown files, PDFs, and chat history.  
This tool turns that fragmented information into a searchable, conversational second brain.

A lightweight, developer-friendly RAG system that runs locally or connects to any OpenAI-compatible API (including Grok).

**Ideal for:**
- Personal knowledge management
- Research paper collections
- Project documentation
- Learning notes and technical journals

---

## Features

- Ingest Markdown, TXT, and PDF files
- Automatic chunking + embedding
- Natural language querying
- Source citations in every answer
- Compatible with OpenAI, Grok, or local models (Ollama)
- Simple CLI interface, easy to extend

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/tahrjatoi/personal-rag-assistant.git
cd personal-rag-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Add your API key (OpenAI / Grok / etc.)

# 4. Add your documents
mkdir -p data
# Drop .md / .txt / .pdf files into the data/ folder

# 5. Ingest documents
python -m src.ingest

# 6. Start chatting
python -m src.chat
```

---

## Project Structure

```text
personal-rag-assistant/
├── data/                 # Place your documents here
├── src/
│   ├── ingest.py         # Document loading & embedding
│   ├── retriever.py      # Vector search logic
│   └── chat.py           # Conversational interface
├── requirements.txt
├── .env.example
└── README.md
```

---

## Example Interaction

```text
You: What did I decide about the RAG architecture last week?

Assistant: According to your notes from 2026-10-20, you decided to use ...
Sources: notes/rag-architecture.md
```

---

## Tech Stack

- **Python 3.10+**
- Vector store (local or managed)
- OpenAI-compatible LLM APIs
- Clean modular design

---

## Possible Extensions

- Web search as a fallback tool
- Notion / Google Drive sync
- Streaming responses
- Multi-user support
- Retrieval quality evaluation harness

---

## Author

**Tahir Jatoi** — AI Engineer  
Focused on practical RAG systems and production LLM applications.

- GitHub: [tahrjatoi](https://github.com/tahrjatoi)
- LinkedIn: [Tahir Jatoi](https://www.linkedin.com/in/tahrjatoi)

---

<div align="center">

*Your notes already contain the answers. This tool just helps you find them.*

</div>
