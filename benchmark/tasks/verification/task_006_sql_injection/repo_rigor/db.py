def get_user(cursor, username):
    query = "SELECT * FROM users WHERE username = ?"
    return cursor.execute(query, (username,)).fetchall()