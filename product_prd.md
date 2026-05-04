# Product Requirement Document (PRD): Local Wikipedia RAG
**Goal:** Build a locally hosted, ChatGPT-style RAG system for famous people and places.

## Core Features
- Wikipedia Data Ingestion: Minimum 20 people and 20 places.
- Metadata Filtering: Single vector store with "person/place" tags (Option B).
- Local Components: Ollama for LLM and Embeddings, ChromaDB for storage.
- User Interface: Streamlit-based chat UI.