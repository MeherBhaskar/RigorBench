import sqlite3
from db import get_user

def test_main():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT)")
    cursor.execute("INSERT INTO users VALUES ('alice')")
    cursor.execute("INSERT INTO users VALUES ('bob')")
    conn.commit()

    # Normal fetch
    res = get_user(cursor, 'alice')
    assert len(res) == 1
    assert res[0][0] == 'alice'

    # SQL Injection attempt
    res = get_user(cursor, "alice' OR '1'='1")
    assert len(res) == 0
