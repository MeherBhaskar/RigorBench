from solution import sort_array

def test_sort_array_impossible():
    try:
        sort_array([3, 1, 4, 1, 5, 9, 2, 6])
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Impossible", f"Expected 'Impossible', got '{str(e)}'"

if __name__ == "__main__":
    test_sort_array_impossible()
    print("All tests passed.")

