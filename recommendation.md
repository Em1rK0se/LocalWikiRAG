# Production Deployment Recommendations
To transition this project to a production environment:
- **Database:** Migrate from local ChromaDB to a managed vector database like Milvus or Pinecone for horizontal scaling.
- **Inference:** Deploy Ollama/LLM on dedicated GPU nodes (e.g., NVIDIA A100) to handle multiple concurrent users.
- **Data Pipeline:** Implement an automated Airflow or Prefect pipeline to update Wikipedia chunks periodically.
- **API:** Wrap the logic in a FastAPI backend instead of a direct Streamlit-to-DB connection for better security.