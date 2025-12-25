from pathlib import Path
from PyPDF2 import PdfReader

SUPPORTED_EXTENSIONS = {".txt", ".pdf"}


def load_documents(folder: Path) -> dict:
    documents = {}

    folder = Path(folder)

    if not folder.exists():
        raise FileNotFoundError(f"Directory not found: {folder}")

    for file in folder.iterdir():
        if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        if file.suffix.lower() == ".txt":
            text = file.read_text(encoding="utf-8", errors="ignore")

        elif file.suffix.lower() == ".pdf":
            reader = PdfReader(file)
            text = " ".join(page.extract_text() or "" for page in reader.pages)

        documents[file.name] = text

    return documents
