from main import longest_identical_sequence

def test_empty():
    assert longest_identical_sequence("") == ("", 0)

def test_single_char():
    assert longest_identical_sequence("a") == ("a", 1)

def test_basic():
    assert longest_identical_sequence("aabbbccccdd") == ("c", 4)

def test_tie():
    assert longest_identical_sequence("aabbcc") == ("a", 2)

def test_interleaved():
    assert longest_identical_sequence("abacadae") == ("a", 1)
