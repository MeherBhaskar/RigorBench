import pytest
from main import sort_array

def test_sort_array_impossible():
    with pytest.raises(ValueError, match='Impossible'):
        sort_array([3, 1, 2])
