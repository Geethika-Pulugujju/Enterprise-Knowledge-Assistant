from backend.app.retrieval.embeddings import EmbeddingModel

model = EmbeddingModel()

vector = model.encode_query(
    "What is the minimum attendance requirement?"
)

print("Embedding dimensions:", len(vector))
print("First 5 values:", vector[:5])