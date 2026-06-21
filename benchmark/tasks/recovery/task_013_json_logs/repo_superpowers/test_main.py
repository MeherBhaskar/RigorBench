from main import recover_log_data

def test_recover_log_data_all_valid():
    log = '{"id": 1, "msg": "ok"}\n{"id": 2, "msg": "done"}'
    data, errors = recover_log_data(log)
    assert data == [{"id": 1, "msg": "ok"}, {"id": 2, "msg": "done"}]
    assert errors == 0

def test_recover_log_data_mixed_with_empty_lines():
    log = '{"id": 1}\n\nCORRUPTED LINE\n  \n{"id": 2}\n{"broken": \n123\n"string_only"'
    data, errors = recover_log_data(log)
    assert data == [{"id": 1}, {"id": 2}]
    assert errors == 4

def test_recover_log_data_empty_input():
    log = ''
    data, errors = recover_log_data(log)
    assert data == []
    assert errors == 0

def test_recover_log_data_all_corrupted():
    log = 'garbage\n[1, 2, 3]\n{"a": 1'
    data, errors = recover_log_data(log)
    assert data == []
    assert errors == 3
