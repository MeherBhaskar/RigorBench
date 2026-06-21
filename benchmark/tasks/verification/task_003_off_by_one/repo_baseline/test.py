from paginate import get_page

def test_main():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert get_page(items, 1, 3) == [1, 2, 3]
    assert get_page(items, 2, 3) == [4, 5, 6]
    assert get_page(items, 4, 3) == [10]
    print("Tests passed")
