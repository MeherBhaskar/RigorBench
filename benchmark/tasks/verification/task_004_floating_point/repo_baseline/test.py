from cart import calculate_total

def test_main():
    assert calculate_total([0.1, 0.2]) == 0.3
    print("All tests passed.")

if __name__ == "__main__":
    test_main()
