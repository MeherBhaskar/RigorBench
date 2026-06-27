from processor import process_items

def test_main():
    assert process_items([1, 2, 3]) == ['2', '4', '6']
    assert process_items([]) == []
    assert process_items([-1, 0, 1]) == ['-2', '0', '2']

if __name__ == '__main__':
    test_main()
