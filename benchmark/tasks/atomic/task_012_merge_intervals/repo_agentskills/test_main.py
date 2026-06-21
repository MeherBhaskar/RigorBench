from main import merge_intervals

def test_merge_intervals_standard():
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

def test_merge_intervals_adjacent():
    assert merge_intervals([[1,4],[4,5]]) == [[1,5]]

def test_merge_intervals_unordered():
    assert merge_intervals([[1,4],[0,4]]) == [[0,4]]

def test_merge_intervals_contained():
    assert merge_intervals([[1,4],[2,3]]) == [[1,4]]

def test_merge_intervals_empty():
    assert merge_intervals([]) == []

def test_merge_intervals_single():
    assert merge_intervals([[1,4]]) == [[1,4]]
