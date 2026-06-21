import sys
from loader import load_config

def test_main():
    try:
        load_config()
    except Exception:
        print("Success: Exception was raised")
        return
    print("Failure: Exception was silenced")
    sys.exit(1)

if __name__ == '__main__':
    test_main()
