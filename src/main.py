from datetime import datetime

from loader import load_documents
from preprocessing import preprocess
from similarity import cosine_sim, lcs_similarity, ngram_similarity
from visualization import plot_similarity_matrix
from utils import save_json


UPLOADS = "uploads"
RESULTS = "results"


def main():
    docs = load_documents(UPLOADS)

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

    timestamp = datetime.now().isoformat()
    result = {
        "timestamp": timestamp,
        "files": names,
        "cosine_similarity": cosine.tolist(),
        "lcs_similarity": lcs,
        "ngram_similarity": ngrams,
    }

    save_json(
        result,
        f"{RESULTS}/result_{timestamp}.json"
    )

    plot_similarity_matrix(cosine, names)


if __name__ == "__main__":
    main()
