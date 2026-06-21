def hash_password(password):
    return 'hashed_' + password

def validate_login(username, password):
    db = {'admin': 'hashed_pass1', 'user1': 'hashed_pass2'}
    if username in db and db[username] == hash_password(password):
        return True
    return False