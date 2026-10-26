from backend.app.retrieval.embeddings import EmbeddingModel
from backend.app.retrieval.vector_store import VectorStore


model = EmbeddingModel()
store = VectorStore()

query = "What is the minimum attendance requirement?"

query_vector = model.encode_query(query)

results = store.search(query_vector, limit=5)

print("\nQuery:", query)
print("\nTop results:\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}")
    print("Score:", result.score)
    print("Page:", result.payload["page_number"])
    print("Source:", result.payload["source"])
    print("Text:", result.payload["text"][:500])
    print("-" * 60)