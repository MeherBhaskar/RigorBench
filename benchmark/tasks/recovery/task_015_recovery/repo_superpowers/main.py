def recover_state(snapshot: dict, wal_logs: list[dict]) -> dict:
    committed_txs = set()
    for log in wal_logs:
        if log['type'] == 'COMMIT':
            committed_txs.add(log['tx_id'])
            
    recovered = snapshot.copy()
    for log in wal_logs:
        if log['tx_id'] in committed_txs and log['type'] == 'SET':
            recovered[log['key']] = log['value']
            
    return recovered
