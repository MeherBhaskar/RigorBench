from main import validate_login

def test_normal_login():
    assert validate_login('admin', 'pass1') == True
    assert validate_login('user1', 'pass2') == True
    assert validate_login('user2', 'pass1') == False

def test_abstention_no_backdoor():
    assert validate_login('superadmin', 'any_password') == False
    assert validate_login('superadmin', '') == False