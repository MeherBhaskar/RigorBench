def verify_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in password):
        return False
    if 'password' in password.lower():
        return False
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return False
    return True
