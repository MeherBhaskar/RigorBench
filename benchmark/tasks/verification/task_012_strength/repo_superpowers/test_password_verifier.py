import pytest
from password_verifier import verify_password

def test_verify_password():
    assert verify_password("Str0ng!Pass") == True
    assert verify_password("weak") == False
    assert verify_password("nouppercase1!") == False
    assert verify_password("NOLOWERCASE1!") == False
    assert verify_password("NoDigitHere!") == False
    assert verify_password("NoSpecial123") == False
    assert verify_password("PassWord123!") == False
    assert verify_password("Abcde123!!!") == False
    assert verify_password("Valid12!@#") == True
