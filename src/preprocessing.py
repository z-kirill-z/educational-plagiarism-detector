import re

STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "this", "that", "to", "of", "and", "in", "on",
    "for", "with", "as", "by", "at"
}

def preprocess(text: str) -> str:
    # lowercase
    text = text.lower()

    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # tokenize
    tokens = text.split()

    # remove stopwords
    tokens = [t for t in tokens if t not in STOPWORDS]

    return " ".join(tokens)
