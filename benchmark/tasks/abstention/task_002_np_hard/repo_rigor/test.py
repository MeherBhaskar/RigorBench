import pytest
from tsp import solve_tsp

def test_main():
    with pytest.raises(NotImplementedError):
        solve_tsp([[0, 1], [1, 0]])
