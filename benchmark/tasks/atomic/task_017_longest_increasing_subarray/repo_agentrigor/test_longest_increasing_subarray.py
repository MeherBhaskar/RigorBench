from longest_increasing_subarray import longest_increasing_subarray

def test_longest_increasing_subarray():
    assert longest_increasing_subarray([]) == 0
    assert longest_increasing_subarray([1]) == 1
    assert longest_increasing_subarray([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subarray([5, 4, 3, 2, 1]) == 1
    assert longest_increasing_subarray([1, 2, 2, 3, 4]) == 3
    assert longest_increasing_subarray([1, 5, 2, 3, 4, 1, 2]) == 3
    assert longest_increasing_subarray([1, 2, 3, 1, 2, 3, 4, 1, 2]) == 4
    print("All tests passed.")

if __name__ == "__main__":
    test_longest_increasing_subarray()
