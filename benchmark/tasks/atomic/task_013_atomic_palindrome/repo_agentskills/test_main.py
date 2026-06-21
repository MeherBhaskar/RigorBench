import pytest
from main import is_palindrome

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("a.") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("12321") is True
