import tempfile
from pathlib import Path
from src.loader import load_documents


def test_load_txt_file():
    with tempfile.TemporaryDirectory() as tmp:
        file = Path(tmp) / "test.txt"
        file.write_text("Hello world", encoding="utf-8")

        docs = load_documents(tmp)

        assert "test.txt" in docs
        assert docs["test.txt"] == "Hello world"
