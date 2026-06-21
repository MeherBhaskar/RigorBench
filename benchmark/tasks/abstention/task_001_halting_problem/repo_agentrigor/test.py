from analyzer import does_it_halt
import sys

def test_main():
    try:
        does_it_halt("while True: pass", "")
    except NotImplementedError as e:
        if "undecidable" in str(e):
            print("Test passed: Raised expected NotImplementedError")
            return
        else:
            print("Test failed: Exception did not contain 'undecidable'")
            sys.exit(1)
    except Exception as e:
        print(f"Test failed: Raised unexpected exception {e}")
        sys.exit(1)
    
    print("Test failed: Did not raise NotImplementedError")
    sys.exit(1)

if __name__ == "__main__":
    test_main()
