from paginate import get_page

def test_main():
    assert get_page([1, 2, 3, 4, 5], 1, 2) == [1, 2]
    assert get_page([1, 2, 3, 4, 5], 2, 2) == [3, 4]
    assert get_page([1, 2, 3, 4, 5], 3, 2) == [5]
