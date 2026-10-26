def create_chunks(
    pages: list[dict],
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[dict]:
    """
    Split page-wise PDF text into overlapping chunks.

    Each chunk keeps its source page number.
    """

    chunks = []

    for page in pages:
        text = page["text"]
        page_number = page["page_number"]

        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append({
                    "text": chunk_text,
                    "page_number": page_number
                })

            start += chunk_size - chunk_overlap

    return chunks