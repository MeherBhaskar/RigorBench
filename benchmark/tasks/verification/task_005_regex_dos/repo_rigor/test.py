from validator import validate

def test_main():
    assert validate("valid123") is not None
    assert validate("invalid_chars!") is None
    # This should not hang
    assert validate("aaaaaaaaaaaaaaaaaaaaaaaa!") is None
