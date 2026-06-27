def recover_state(snapshot: dict, wal_logs: list[dict]) -> dict:
    state = snapshot.copy()
    
    committed_txs = set()
    for log in wal_logs:
        if log['type'] == 'COMMIT':
            committed_txs.add(log['tx_id'])
            
    for log in wal_logs:
        if log['tx_id'] in committed_txs and log['type'] == 'SET':
            state[log['key']] = log['value']
            
    return state
