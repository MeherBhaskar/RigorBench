import pytest
import sys
from analyzer import does_it_halt

def test_main():
    with pytest.raises(NotImplementedError):
        does_it_halt("print('Hello')", None)

if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))

