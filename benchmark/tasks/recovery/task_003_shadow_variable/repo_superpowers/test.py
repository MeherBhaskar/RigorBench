from processor import process_items

def test_main():
    assert process_items([1, 2, 3]) == ['2', '4', '6']
