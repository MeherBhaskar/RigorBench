from main import recover_system

def test_recover_update_and_create():
    current_state = {
        "file1.txt": "corrupted",
        "file2.txt": "newly created"
    }
    undo_log = [
        "CREATE file2.txt",
        "UPDATE file1.txt valid data"
    ]
    expected = {
        "file1.txt": "valid data"
    }
    assert recover_system(current_state, undo_log) == expected

def test_recover_delete():
    current_state = {
        "other.txt": "safe"
    }
    undo_log = [
        "DELETE missing.txt lost data with spaces"
    ]
    expected = {
        "other.txt": "safe",
        "missing.txt": "lost data with spaces"
    }
    assert recover_system(current_state, undo_log) == expected

def test_no_undo_needed():
    current_state = {"a.txt": "a"}
    undo_log = []
    assert recover_system(current_state, undo_log) == {"a.txt": "a"}

def test_multiple_operations_same_file():
    current_state = {
        "file.txt": "latest"
    }
    # Reverse order: first undo UPDATE (restores 'intermediate'), then undo CREATE (removes it)
    undo_log = [
        "CREATE file.txt",
        "UPDATE file.txt intermediate"
    ]
    expected = {}
    assert recover_system(current_state, undo_log) == expected
