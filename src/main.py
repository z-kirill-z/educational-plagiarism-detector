from datetime import datetime
from pathlib import Path

from loader import load_documents
from preprocessing import preprocess
from similarity import cosine_sim, lcs_similarity, ngram_similarity
from visualization import plot_similarity_matrix
from utils import save_json


BASE_DIR = Path(__file__).resolve().parent.parent

UPLOADS_DIR = BASE_DIR / "uploads"
RESULTS_DIR = BASE_DIR / "results"


def main():
    docs = load_documents(UPLOADS_DIR)

    if not docs:
        print("No documents found in uploads directory.")
        return

    names = list(docs.keys())
    texts = [preprocess(docs[name]) for name in names]

    cosine = cosine_sim(texts)

    lcs = {
        f"{a}-{b}": lcs_similarity(texts[i], texts[j])
        for i, a in enumerate(names)
        for j, b in enumerate(names)
        if i < j
    }

    ngrams = {
        f"{a}-{b}": ngram_similarity(texts[i], texts[j])
        for i, a in enumerate(names)
        for j, b in enumerate(names)
        if i < j
    }

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    result = {
        "timestamp": timestamp,
        "files": names,
        "cosine_similarity": cosine.tolist(),
        "lcs_similarity": lcs,
        "ngram_similarity": ngrams,
    }

    result_path = RESULTS_DIR / f"result_{timestamp}.json"
    save_json(result, result_path)
    plot_similarity_matrix(cosine, names)


if __name__ == "__main__":
    main()
