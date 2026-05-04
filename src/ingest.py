import wikipediaapi
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Required entities for the assignment
PEOPLE = [
    "Albert Einstein", "Marie Curie", "Leonardo da Vinci", "William Shakespeare",
    "Ada Lovelace", "Nikola Tesla", "Lionel Messi", "Cristiano Ronaldo",
    "Taylor Swift", "Frida Kahlo", "Isaac Newton", "Stephen Hawking", "Charles Darwin",
    "Galileo Galilei", "Nelson Mandela", "Malala Yousafzai", "Vincent van Gogh",
    "Wolfgang Amadeus Mozart", "Pablo Picasso", "Queen Elizabeth II"
]

PLACES = [
    "Eiffel Tower", "Great Wall of China", "Taj Mahal", "Grand Canyon",
    "Machu Picchu", "Colosseum", "Hagia Sophia", "Statue of Liberty",
    "Pyramids of Giza", "Mount Everest", "Stonehenge", "Petra", "Niagara Falls",
    "Santorini", "Venice", "Great Barrier Reef", "Angkor Wat", "Chichen Itza",
    "Easter Island", "Burj Khalifa"
]

def fetch_wiki_data(topic):
    """
    Fetches raw text content from Wikipedia using a descriptive User-Agent.
    """
    wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent="LocalWikiRAG/1.0 (contact: your_email@itu.edu.tr)"
    )
    page = wiki.page(topic)
    return page.text if page.exists() else None

def process_and_store():
    """
    Processes Wikipedia data: Ingest -> Chunk -> Store in ChromaDB.
    """
    # Initialize local ChromaDB (Option B: One store with metadata)
    client = chromadb.PersistentClient(path="./data/chroma_db")
    collection = client.get_or_create_collection(name="wiki_rag")

    # Strategy: Recursive chunking (1000 characters with 100 overlap)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    combined_list = [("person", p) for p in PEOPLE] + [("place", pl) for pl in PLACES]

    for category, name in combined_list:
        print(f"Downloading and processing: {name}...")
        raw_text = fetch_wiki_data(name)
        
        if raw_text:
            chunks = text_splitter.split_text(raw_text)
            
            # Metadata allows the system to filter by category during retrieval
            metadatas = [{"name": name, "type": category} for _ in chunks]
            ids = [f"{name.replace(' ', '_')}_{i}" for i in range(len(chunks))]
            
            collection.add(
                documents=chunks,
                metadatas=metadatas,
                ids=ids
            )

if __name__ == "__main__":
    process_and_store()
    print("\nSuccess: Data has been ingested and stored locally in /data/chroma_db")