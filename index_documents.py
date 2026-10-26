from backend.app.ingestion.pdf_loader import extract_pages_from_pdf
from backend.app.ingestion.chunker import create_chunks
from backend.app.retrieval.embeddings import EmbeddingModel
from backend.app.retrieval.vector_store import VectorStore


PDF_PATH = "data/mru_academic_regulations_r23.pdf"


print("Loading PDF...")

pages = extract_pages_from_pdf(PDF_PATH)

print("Creating chunks...")

chunks = create_chunks(pages)

print("Generating embeddings...")

model = EmbeddingModel()

vectors = model.encode_texts(
    [chunk["text"] for chunk in chunks]
)

print("Connecting to Qdrant...")

vector_store = VectorStore()

vector_store.create_collection()

print("Storing documents in Qdrant...")

count = vector_store.add_documents(chunks, vectors)

print()
print("========== INDEXING COMPLETE ==========")
print("Pages:", len(pages))
print("Chunks:", len(chunks))
print("Embeddings:", len(vectors))
print("Vectors stored in Qdrant:", count)
print("========================================")