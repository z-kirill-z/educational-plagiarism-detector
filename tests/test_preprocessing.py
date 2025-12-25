from src.preprocessing import preprocess


def test_preprocess_lowercase():
    text = "Hello WORLD"
    result = preprocess(text)
    assert result == "hello world"


def test_preprocess_removes_punctuation():
    text = "Hello, world!!!"
    result = preprocess(text)
    assert "!" not in result
    assert "," not in result


def test_preprocess_removes_stopwords():
    text = "This is a simple test"
    result = preprocess(text)
    assert "is" not in result
    assert "this" not in result
