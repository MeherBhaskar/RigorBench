from main import is_palindrome

def test_palindrome_basic():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_palindrome_false():
    assert is_palindrome("race a car") is False

def test_palindrome_empty():
    assert is_palindrome(" ") is True

def test_palindrome_numbers():
    assert is_palindrome("0P") is False
    assert is_palindrome("1b1") is True

def test_palindrome_symbols():
    assert is_palindrome(".,") is True