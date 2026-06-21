import sqlite3
from db import get_user

def test_main():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, id INTEGER)")
    cursor.execute("INSERT INTO users VALUES ('admin', 1)")
    conn.commit()
    
    # Test normal
    res = get_user(cursor, "admin")
    assert len(res) == 1
    
    # Test SQL injection
    res = get_user(cursor, "admin' OR '1'='1")
    assert len(res) == 0

if __name__ == '__main__':
    test_main()
    print("Tests passed.")
