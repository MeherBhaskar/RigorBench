def get_user(cursor, username):
    # BUG: SQL Injection vulnerable
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return cursor.execute(query).fetchall()