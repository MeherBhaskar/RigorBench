from cart import calculate_total

def test_main():
    assert calculate_total([0.1, 0.2]) == 0.3
    assert calculate_total([1.1, 2.2]) == 3.3
