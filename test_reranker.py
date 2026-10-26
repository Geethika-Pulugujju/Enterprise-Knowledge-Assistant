from hybrid_retriever import HybridRetriever
from reranker import Reranker


query = "What is the minimum attendance requirement?"

print("Running Hybrid Search...")

retriever = HybridRetriever()

results = retriever.search(
    query,
    limit=10
)

print("Hybrid results:", len(results))

print("\nRunning Cross-Encoder Reranking...")

reranker = Reranker()

reranked_results = reranker.rerank(
    query,
    results,
    top_k=5
)

print("\n========== RERANKED RESULTS ==========\n")

for i, result in enumerate(reranked_results, start=1):

    print(f"Result {i}")
    print("Rerank Score:", result["rerank_score"])
    print("RRF Score:", result["rrf_score"])
    print("Page:", result["page_number"])
    print("Text:", result["text"][:500])

    print("-" * 60)