import pytest
from password_verifier import verify_password

def test_verify_password():
    # Valid passwords
    assert verify_password("Str0ng!Pass") == True
    assert verify_password("Valid12!@#") == True
    assert verify_password("Abc1234!") == True
    assert verify_password("P@ss12345") == True
    assert verify_password("A_b_c_1_2") == True
    
    # Too short
    assert verify_password("weak") == False
    assert verify_password("Ab1!cde") == False
    assert verify_password("") == False
    
    # Missing uppercase
    assert verify_password("nouppercase1!") == False
    
    # Missing lowercase
    assert verify_password("NOLOWERCASE1!") == False
    
    # Missing digit
    assert verify_password("NoDigitHere!") == False
    
    # Missing special character
    assert verify_password("NoSpecial123") == False
    
    # Contains "password" case-insensitive
    assert verify_password("PassWord123!") == False
    assert verify_password("password123!") == False
    assert verify_password("PASSWORD123!") == False
    assert verify_password("123password!") == False
    assert verify_password("PassWord!123") == False
    
    # 3 consecutive identical characters
    assert verify_password("Abcde123!!!") == False
    assert verify_password("aaa123!A") == False
    assert verify_password("Abcde123aaa!!!") == False
    assert verify_password("Abccc123!") == False
    assert verify_password("Abc12333!") == False

