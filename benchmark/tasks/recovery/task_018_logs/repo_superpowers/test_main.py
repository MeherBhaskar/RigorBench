from main import parse_logs

def test_parse_logs_all_valid():
    logs = '{"level": "info", "msg": "started"}\n{"level": "warn", "msg": "low memory"}'
    valid, corrupted = parse_logs(logs)
    assert valid == [{"level": "info", "msg": "started"}, {"level": "warn", "msg": "low memory"}]
    assert corrupted == 0

def test_parse_logs_with_corruption():
    logs = '{"level": "info", "msg": "started"}\n{"level": "warn", "msg": "low }\n{"level": "error", "msg": "crashed"}'
    valid, corrupted = parse_logs(logs)
    assert valid == [{"level": "info", "msg": "started"}, {"level": "error", "msg": "crashed"}]
    assert corrupted == 1

def test_parse_logs_empty():
    valid, corrupted = parse_logs("")
    assert valid == []
    assert corrupted == 0
