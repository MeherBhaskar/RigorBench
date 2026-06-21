import pytest
from main import is_balanced

def test_is_balanced():
    assert is_balanced('()') is True
    assert is_balanced('()[]{}') is True
    assert is_balanced('(]') is False
    assert is_balanced('([)]') is False
    assert is_balanced('{[]}') is True
    assert is_balanced('') is True
    assert is_balanced('(') is False
    assert is_balanced('}') is False
