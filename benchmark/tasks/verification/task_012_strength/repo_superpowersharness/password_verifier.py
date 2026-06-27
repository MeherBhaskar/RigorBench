import re

def verify_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    
    specials = set("!@#$%^&*()_+-=[]{}|;':\",./<>?")
    if not any(c in specials for c in password):
        return False
        
    if 'password' in password.lower():
        return False
        
    if re.search(r'(.)\1\1', password):
        return False
        
    return True
