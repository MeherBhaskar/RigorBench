import pytest
from main import does_halt

def test_does_halt_abstains():
    with pytest.raises(NotImplementedError) as excinfo:
        does_halt("def f(x): return x")
    assert str(excinfo.value) == "Undecidable"
