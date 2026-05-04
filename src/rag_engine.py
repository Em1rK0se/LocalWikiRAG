import ollama
import chromadb

class RAGEngine:
    def __init__(self):
        """
        Initializes the RAG Engine by connecting to the local ChromaDB vector store.
        """
        # Connection to the persistent database folder we created
        self.client = chromadb.PersistentClient(path="./data/chroma_db")
        self.collection = self.client.get_collection(name="wiki_rag")
        self.model_name = "llama3.2"

    def query_router(self, query):
        """
        Simple rule-based logic to determine if the query is about a person or a place.
        Requirement: The system should determine whether the query is about a person or a place.
        """
        query_lower = query.lower()
        person_keywords = ["who", "born", "invented", "discovered", "played", "career"]
        place_keywords = ["where", "located", "built", "height", "visit", "country"]

        is_person = any(k in query_lower for k in person_keywords)
        is_place = any(k in query_lower for k in place_keywords)

        if is_person and not is_place:
            return "person"
        elif is_place and not is_person:
            return "place"
        return None  # Searches everything if logic can't decide

    def retrieve_context(self, query, n_results=3):
        """
        Searches the local vector store for relevant document chunks.
        Applies metadata filtering based on the router's decision.
        """
        category = self.query_router(query)
        
        # Option B requirement: Metadata filtering (type equals person or place)
        where_filter = {"type": category} if category else None

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_filter
        )
        
        return results['documents'][0] if results['documents'] else []

    def generate_answer(self, query, context):
        """
        Generates an answer using the local language model.
        Requirement: Answer must be grounded in context and say 'I don't know' if missing.[cite: 1]
        """
        if not context:
            return "I don't know. The requested information is not in my local database."

        # Explicit instruction to prevent hallucinations
        prompt = f"""
        INSTRUCTIONS: Answer the question using ONLY the provided context.
        If the information is not present in the context, say "I don't know".
        
        CONTEXT:
        {" ".join(context)}
        
        QUESTION: {query}
        
        ANSWER:
        """

        response = ollama.generate(model=self.model_name, prompt=prompt)
        return response['response']

# Academic test to ensure the logic works before launching the UI
if __name__ == "__main__":
    engine = RAGEngine()
    test_q = "What did Nikola Tesla discover?"
    ctx = engine.retrieve_context(test_q)
    print(f"Test Question: {test_q}\nResult: {engine.generate_answer(test_q, ctx)}")