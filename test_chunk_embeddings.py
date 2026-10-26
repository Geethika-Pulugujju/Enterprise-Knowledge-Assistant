from backend.app.ingestion.pdf_loader import extract_pages_from_pdf
from backend.app.ingestion.chunker import create_chunks
from backend.app.retrieval.embeddings import EmbeddingModel

pages = extract_pages_from_pdf(
    "data/mru_academic_regulations_r23.pdf"
)

chunks = create_chunks(pages)

model = EmbeddingModel()

vectors = model.encode_texts(
    [chunk["text"] for chunk in chunks]
)

print("Pages:", len(pages))
print("Chunks:", len(chunks))
print("Embeddings:", len(vectors))
print("Embedding dimension:", len(vectors[0]))