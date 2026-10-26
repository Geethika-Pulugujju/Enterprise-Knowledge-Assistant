from fastapi import FastAPI
from pydantic import BaseModel

from hybrid_retriever import HybridRetriever
from reranker import Reranker
from backend.app.generation.answer_generator import AnswerGenerator


app = FastAPI(
    title="Enterprise Knowledge Assistant",
    description="RAG-powered domain expert chatbot",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


# Initialize RAG components
retriever = HybridRetriever()
reranker = Reranker()
answer_generator = AnswerGenerator()


@app.get("/")
def root():
    return {
        "message": "Enterprise Knowledge Assistant API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    # Step 1: Hybrid retrieval
    results = retriever.search(
        request.question,
        limit=10
    )

    # Step 2: Cross-encoder reranking
    reranked_results = reranker.rerank(
        request.question,
        results,
        top_k=5
    )

    # Step 3: Generate grounded answer
    response = answer_generator.generate(
        request.question,
        reranked_results
    )

    return response