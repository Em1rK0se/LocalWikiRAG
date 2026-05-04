# 🤖 Local Wikipedia RAG Assistant

This project is a high-performance, fully local **Retrieval-Augmented Generation (RAG)** system developed for the **BLG483E - AI Aided Computer Engineering** course (Project 3) at Istanbul Technical University. It allows users to query information about 20 famous people and 20 famous places using only local resources.

## 🌟 Key Features
- **Total Privacy:** Runs entirely on `localhost`. No external LLM APIs are used.
- **Smart Routing:** Uses a rule-based query router to distinguish between people and places for optimized retrieval using metadata.
- **Advanced UI/UX:** Features a Streamlit-based chat interface with real-time response streaming and latency measurement.
- **High-Quality Chunking:** Implements a `RecursiveCharacterTextSplitter` strategy with defined chunk sizes and overlaps to maintain context integrity.
- **Academic Rigor:** Designed with explicit grounding to avoid hallucinations. If the information is not in the local database, the system strictly returns "I don't know".

## 🛠️ Tech Stack
- **Language:** Python 3.11+
- **LLM Engine:** Ollama (Llama 3.2 3B)
- **Embeddings:** Nomic-Embed-Text via Ollama
- **Vector Database:** ChromaDB
- **Frontend:** Streamlit
- **Data Source:** Wikipedia-API

## 📂 Project Structure
- `src/ingest.py`: Script for fetching Wikipedia data, chunking, and populating ChromaDB.
- `src/rag_engine.py`: The core RAG logic, handles retrieval, routing, and LLM generation.
- `src/app.py`: The Streamlit web application providing the chat interface and streaming logic.
- `product_prd.md`: Product Requirement Document detailing the project scope.
- `recommendation.md`: Professional advice for production-level scaling.

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have **Ollama** installed on your Mac. If not, download it from [ollama.com](https://ollama.com).

### 2. Environment Setup
Clone the repository and create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
