import pytest
from tsp import solve_tsp

def test_main():
    with pytest.raises(NotImplementedError, match="NP-hard"):
        solve_tsp([])
