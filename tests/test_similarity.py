from src.similarity import lcs_similarity, ngram_similarity


def test_lcs_identical_texts():
    assert lcs_similarity("abc def", "abc def") == 1.0


def test_lcs_different_texts():
    assert lcs_similarity("abc", "xyz") < 0.5


def test_ngram_similarity_zero():
    assert ngram_similarity("one two three", "four five six") == 0.0
