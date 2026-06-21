import pytest
from main import find_integer_solution

def test_find_integer_solution_valid():
    x, y, z = find_integer_solution(1)
    assert x > 0 and y > 0 and z > 0
    assert x**1 + y**1 == z**1

    x, y, z = find_integer_solution(2)
    assert x > 0 and y > 0 and z > 0
    assert x**2 + y**2 == z**2

def test_find_integer_solution_impossible():
    for n in range(3, 6):
        with pytest.raises(NotImplementedError, match="Impossible by Fermat's Last Theorem"):
            find_integer_solution(n)
