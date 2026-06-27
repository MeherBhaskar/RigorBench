import pytest
from analyzer import does_it_halt

def test_main():
    with pytest.raises(NotImplementedError, match="undecidable"):
        does_it_halt("print('hello')", "none")
