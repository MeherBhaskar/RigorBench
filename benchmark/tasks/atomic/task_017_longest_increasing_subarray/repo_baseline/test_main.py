import pytest
from main import longest_increasing_subarray

def test_longest_increasing_subarray():
    assert longest_increasing_subarray([1, 3, 5, 4, 7]) == 3
    assert longest_increasing_subarray([2, 2, 2, 2, 2]) == 1
    assert longest_increasing_subarray([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subarray([5, 4, 3, 2, 1]) == 1
    assert longest_increasing_subarray([]) == 0
    assert longest_increasing_subarray([1]) == 1
