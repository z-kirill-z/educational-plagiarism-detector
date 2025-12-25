from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher


def cosine_sim(texts: list[str]) -> list[list[float]]:
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(texts)
    return cosine_similarity(tfidf)


def lcs_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def ngram_similarity(a: str, b: str, n=3) -> float:
    def ngrams(text):
        tokens = text.split()
        return set(tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1))

    na = ngrams(a)
    nb = ngrams(b)

    if not na or not nb:
        return 0.0

    return len(na & nb) / len(na | nb)
