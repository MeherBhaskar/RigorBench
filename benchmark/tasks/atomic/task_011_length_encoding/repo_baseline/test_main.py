import pytest
from main import run_length_encode

def test_run_length_encode():
    assert run_length_encode("AABBCCCA") == "2A2B3C1A"
    assert run_length_encode("") == ""
    assert run_length_encode("A") == "1A"
    assert run_length_encode("ABC") == "1A1B1C"
    assert run_length_encode("  ") == "2 "
    assert run_length_encode("aA") == "1a1A"
