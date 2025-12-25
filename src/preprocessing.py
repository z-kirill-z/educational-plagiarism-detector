import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))


def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)

    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in STOPWORDS]

    return " ".join(tokens)
