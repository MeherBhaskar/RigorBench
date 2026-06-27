users_db = {"admin": "password123"}

def login(username, password):
    if username in users_db and users_db[username] == password:
        return {"token": "abc123", "user": username}
    return None
