import pytest
from main import extract_domain

def test_extract_domain_valid():
    assert extract_domain("user@example.com") == "example.com"
    assert extract_domain("first.last@sub.domain.org") == "sub.domain.org"

def test_extract_domain_invalid():
    with pytest.raises(ValueError):
        extract_domain("invalid-email-no-at")
    with pytest.raises(ValueError):
        extract_domain("just_a_string")
