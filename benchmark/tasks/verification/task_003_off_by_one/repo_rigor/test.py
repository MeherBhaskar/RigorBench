from paginate import get_page

def test_main():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Page 1, size 3
    page1 = get_page(items, 1, 3)
    assert page1 == [1, 2, 3]
    
    # Page 2, size 3
    page2 = get_page(items, 2, 3)
    assert page2 == [4, 5, 6]
    
    # Page 4, size 3
    page4 = get_page(items, 4, 3)
    assert page4 == [10]
