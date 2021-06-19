import pytest
from ie_utils import tokenization


@pytest.mark.parametrize("sentence, expected_tokens", [
    ("This is a sentence", ["This", "is", "a", "sentence"]),
    ("Another test", ["Another", "test"]),
])

def test_tokenize_returns_expected_list(sentence, expected_tokens):
    tokens = tokenization(sentence)
    
    assert tokens == expected_tokens
    
def test_tokenize_lower_returns_lowercase_tokens():
    sentence = "This is a sentence"
    expected_tokens = ["this", "is", "a", "sentence"]
    tokens = tokenization(sentence, lower=True)
    
    assert tokens == expected_tokens