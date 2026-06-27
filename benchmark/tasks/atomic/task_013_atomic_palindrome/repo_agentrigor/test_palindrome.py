import pytest
from palindrome import is_palindrome

def test_is_palindrome_basic():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_is_palindrome_ignore_non_alphanumeric():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race car!") == True

def test_is_palindrome_case_insensitive():
    assert is_palindrome("RaceCar") == True

def test_is_palindrome_empty_or_no_alphanumeric():
    assert is_palindrome("") == True
    assert is_palindrome(".,?!") == True
    assert is_palindrome(" ") == True
