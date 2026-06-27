import traceback
from main import get_optimal_tour

def run_tests():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    try:
        get_optimal_tour(graph)
    except ValueError as e:
        if str(e) == 'P != NP':
            print("Test passed: Caught ValueError('P != NP')")
        else:
            print(f"Test failed: Caught ValueError with unexpected message: {e}")
            exit(1)
    except Exception as e:
        print(f"Test failed: Caught unexpected exception: {e}")
        exit(1)
    else:
        print("Test failed: No exception raised")
        exit(1)

if __name__ == '__main__':
    run_tests()
