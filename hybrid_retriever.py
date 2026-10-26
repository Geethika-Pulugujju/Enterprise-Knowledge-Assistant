from rank_bm25 import BM25Okapi

from backend.app.ingestion.pdf_loader import extract_pages_from_pdf
from backend.app.ingestion.chunker import create_chunks
from backend.app.retrieval.embeddings import EmbeddingModel
from backend.app.retrieval.vector_store import VectorStore


class HybridRetriever:

    def __init__(self):
        # Load the document chunks
        pages = extract_pages_from_pdf(
            "data/mru_academic_regulations_r23.pdf"
        )

        self.chunks = create_chunks(pages)

        # Prepare BM25
        tokenized_chunks = [
            chunk["text"].lower().split()
            for chunk in self.chunks
        ]

        self.bm25 = BM25Okapi(tokenized_chunks)

        # Prepare semantic search
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def search(self, query: str, limit: int = 5):

        # -----------------------------
        # 1. Semantic Search
        # -----------------------------
        query_vector = self.embedding_model.encode_query(query)

        dense_results = self.vector_store.search(
            query_vector,
            limit=10
        )

        # -----------------------------
        # 2. BM25 Keyword Search
        # -----------------------------
        tokenized_query = query.lower().split()

        bm25_scores = self.bm25.get_scores(tokenized_query)

        bm25_ranked = sorted(
            range(len(bm25_scores)),
            key=lambda i: bm25_scores[i],
            reverse=True
        )[:10]

        # -----------------------------
        # 3. Reciprocal Rank Fusion
        # -----------------------------
        rrf_scores = {}

        k = 60

        # Dense results
        for rank, result in enumerate(dense_results, start=1):

            chunk_text = result.payload["text"]

            matching_index = next(
                (
                    i
                    for i, chunk in enumerate(self.chunks)
                    if chunk["text"] == chunk_text
                ),
                None
            )

            if matching_index is not None:
                rrf_scores[matching_index] = (
                    rrf_scores.get(matching_index, 0)
                    + 1 / (k + rank)
                )

        # BM25 results
        for rank, index in enumerate(bm25_ranked, start=1):

            rrf_scores[index] = (
                rrf_scores.get(index, 0)
                + 1 / (k + rank)
            )

        # Sort by combined RRF score
        ranked_results = sorted(
            rrf_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Return top results
        results = []

        for index, score in ranked_results[:limit]:

            result = self.chunks[index].copy()

            result["rrf_score"] = score

            results.append(result)

        return results