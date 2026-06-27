def recover_state(snapshot: dict, wal_logs: list[dict]) -> dict:
    committed_txs = set()
    for log in wal_logs:
        if log.get("type") == "COMMIT":
            committed_txs.add(log.get("tx_id"))
            
    recovered_state = snapshot.copy()
    for log in wal_logs:
        if log.get("type") == "SET" and log.get("tx_id") in committed_txs:
            recovered_state[log.get("key")] = log.get("value")
            
    return recovered_state
