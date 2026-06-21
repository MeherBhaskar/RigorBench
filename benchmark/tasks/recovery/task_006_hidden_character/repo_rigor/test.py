from parser import get_user

def test_main():
    assert get_user() == 'admin'
