from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


class VectorStore:
    def __init__(self):
        self.client = QdrantClient(path="data/qdrant")
        self.collection_name = "mru_knowledge"

    def create_collection(self):
        collections = self.client.get_collections().collections

        if self.collection_name not in [c.name for c in collections]:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def add_documents(self, chunks, vectors):
        points = []

        for index, (chunk, vector) in enumerate(zip(chunks, vectors)):
            points.append(
                PointStruct(
                    id=index,
                    vector=vector.tolist(),
                    payload={
                        "text": chunk["text"],
                        "page_number": chunk["page_number"],
                        "source": "mru_academic_regulations_r23.pdf"
                    }
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

        return len(points)

    def search(self, query_vector, limit=5):
        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector.tolist(),
            limit=limit,
            with_payload=True
        )

        return results.points