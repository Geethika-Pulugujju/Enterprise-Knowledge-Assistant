from pathlib import Path
from pypdf import PdfReader


def extract_pages_from_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF while preserving page numbers.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    reader = PdfReader(str(path))

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text:
            pages.append({
                "page_number": page_number,
                "text": text.strip()
            })

    return pages