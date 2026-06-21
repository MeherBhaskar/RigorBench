import pytest
from main import binary_search

def test_precondition_unsorted():
    with pytest.raises(ValueError, match="Array must be sorted"):
        binary_search([3, 1, 2], 2)

def test_binary_search_correctness():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([5], 5) == 0
    assert binary_search([], 5) == -1

def test_source_code_contains_contracts():
    with open("main.py", "r") as f:
        content = f.read()
        assert "ValueError" in content, "Precondition ValueError not raised"
        assert "RuntimeError" in content, "Postcondition RuntimeError not raised"
