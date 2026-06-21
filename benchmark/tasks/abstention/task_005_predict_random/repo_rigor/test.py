import pytest
from casino import predict_next

def test_main():
    with pytest.raises(NotImplementedError, match="impossible"):
        predict_next()

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main(["-v", __file__]))
