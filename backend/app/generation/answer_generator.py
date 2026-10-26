import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class AnswerGenerator:

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is not configured in the .env file."
            )

        self.client = Groq(api_key=api_key)

    def generate(self, query: str, results: list[dict]):

        if not results:
            return {
                "answer": (
                    "I could not find relevant information "
                    "in the university knowledge base."
                ),
                "sources": []
            }

        # Use the top retrieved results as the grounded context
        context_parts = []

        for result in results[:3]:
            context_parts.append(
                f"[Page {result['page_number']}]\n"
                f"{result['text']}"
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
Answer the user's question using ONLY the information provided
in the context below.

Rules:
- Do not use outside knowledge.
- Do not invent or assume information.
- If the answer is not present in the context, say that the
  information was not found in the knowledge base.
- Give a clear and concise answer.
- Mention the relevant page number when appropriate.

Context:
{context}

User Question:
{query}
"""

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an Enterprise Knowledge Assistant. "
                        "Provide accurate, grounded answers using "
                        "only the supplied context."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        answer = response.choices[0].message.content

        sources = []

        for result in results:
            sources.append({
                "source": result.get(
                    "source",
                    "mru_academic_regulations_r23.pdf"
                ),
                "page": result["page_number"]
            })

        return {
            "answer": answer,
            "sources": sources
        }