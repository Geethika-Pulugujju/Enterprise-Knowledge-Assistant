from hybrid_retriever import HybridRetriever


retriever = HybridRetriever()

query = "What is the minimum attendance requirement?"

results = retriever.search(query, limit=5)

print("\nQuery:", query)
print("\nHybrid Search Results:\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}")
    print("RRF Score:", result["rrf_score"])
    print("Page:", result["page_number"])
    print("Source:", result.get("source", "mru_academic_regulations_r23.pdf"))
    print("Text:", result["text"][:500])
    print("-" * 60)