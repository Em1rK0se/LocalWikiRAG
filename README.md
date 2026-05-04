# 🤖 Local Wikipedia RAG Assistant

This project is a high-performance, fully local **Retrieval-Augmented Generation (RAG)** system developed for the **BLG483E - AI Aided Computer Engineering** course (Project 3) at Istanbul Technical University.

## 🎥 Demo Video
**[https://www.loom.com/share/d0a9c76629b34efdaa70c40c36bf0b56]**  

## 🌟 Key Features
- **Total Privacy:** Runs entirely on `localhost`. No external LLM APIs are used.
- **Smart Routing:** Uses a rule-based query router to distinguish between people and places using metadata tags.
- **Advanced UI/UX:** Features a Streamlit-based chat interface with real-time response streaming and latency measurement.
- **Academic Rigor:** Designed with explicit grounding to avoid hallucinations. If information is not in the local database, it strictly returns "I don't know".

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
- `src/app.py`: The Streamlit web application providing the chat interface.
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
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Local Models (Ollama)
The system requires specific models to be available locally. Run the following commands:
```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 5. Ingest Data
Before starting the application, populate the local vector database with Wikipedia data:
```bash
python src/ingest.py
```

### 6. Run the Application
Start the Streamlit interface:
```bash
streamlit run src/app.py
```

## ❓ Example Queries to Try
Once the application is running, you can test the following scenarios:
- **People:** "Who was Albert Einstein and what is he known for?"
- **Places:** "Where is the Eiffel Tower located?"
- **Comparison:** "Compare Albert Einstein and Nikola Tesla."
- **Failure Case:** "Who is the president of Mars?" (Expected response: "I don't know")
```