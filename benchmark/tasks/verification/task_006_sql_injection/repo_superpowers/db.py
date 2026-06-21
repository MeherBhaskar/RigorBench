def get_user(cursor, username):
    # BUG: SQL Injection vulnerable
    query = "SELECT * FROM users WHERE username = ?"
    return cursor.execute(query, (username,)).fetchall()