import pytest
from main import recover_state

def test_no_transactions():
    wal = [
        "SET a 1",
        "SET b 2",
        "DELETE a"
    ]
    assert recover_state(wal) == {"b": "2"}

def test_committed_transaction():
    wal = [
        "SET a 1",
        "BEGIN",
        "SET a 2",
        "SET b 3",
        "COMMIT"
    ]
    assert recover_state(wal) == {"a": "2", "b": "3"}

def test_rolled_back_transaction():
    wal = [
        "SET a 1",
        "BEGIN",
        "SET a 2",
        "SET b 3",
        "ROLLBACK",
        "SET c 4"
    ]
    assert recover_state(wal) == {"a": "1", "c": "4"}

def test_incomplete_transaction():
    wal = [
        "SET a 1",
        "BEGIN",
        "SET a 2",
        "SET b 3"
    ]
    # The transaction never committed, so its changes are lost
    assert recover_state(wal) == {"a": "1"}

def test_multiple_transactions():
    wal = [
        "BEGIN",
        "SET user1 alice",
        "COMMIT",
        "BEGIN",
        "SET user2 bob",
        "ROLLBACK",
        "BEGIN",
        "SET user3 charlie"
    ]
    assert recover_state(wal) == {"user1": "alice"}
