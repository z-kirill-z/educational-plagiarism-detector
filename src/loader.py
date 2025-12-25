from pathlib import Path
from PyPDF2 import PdfReader

SUPPORTED_EXTENSIONS = {".txt", ".pdf"}


def load_documents(folder: str) -> dict:
    documents = {}

    for file in Path(folder).iterdir():
        if file.suffix not in SUPPORTED_EXTENSIONS:
            continue

        if file.suffix == ".txt":
            text = file.read_text(encoding="utf-8", errors="ignore")

        elif file.suffix == ".pdf":
            reader = PdfReader(file)
            text = " ".join(page.extract_text() or "" for page in reader.pages)

        documents[file.name] = text

    return documents
