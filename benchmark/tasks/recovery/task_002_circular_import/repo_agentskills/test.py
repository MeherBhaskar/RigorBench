from a import a_func
from b import b_func

def test_main():
    assert a_func() == 'b'
    assert b_func() == 'b'

if __name__ == "__main__":
    test_main()
