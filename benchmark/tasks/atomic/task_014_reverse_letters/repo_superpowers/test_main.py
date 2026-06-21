from main import reverse_letters

def test_reverse_letters_basic():
    assert reverse_letters("ab-cd") == "dc-ba"

def test_reverse_letters_complex():
    assert reverse_letters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"

def test_reverse_letters_numbers():
    assert reverse_letters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg-ntse-T!"

def test_reverse_letters_no_letters():
    assert reverse_letters("123-456=789") == "123-456=789"

def test_reverse_letters_only_letters():
    assert reverse_letters("abcdef") == "fedcba"

def test_reverse_letters_empty():
    assert reverse_letters("") == ""
