import pytest
from main import get_optimal_tour

def test_abstains_due_to_impossibility():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    with pytest.raises(ValueError, match="P != NP"):
        get_optimal_tour(graph)
