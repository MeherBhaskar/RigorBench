def recover_state(snapshot: dict, wal_logs: list[dict]) -> dict:
    state = snapshot.copy()
    committed_txs = set()
    aborted_txs = set()
    
    for log in wal_logs:
        if log['type'] == 'COMMIT':
            committed_txs.add(log['tx_id'])
        elif log['type'] == 'ABORT':
            aborted_txs.add(log['tx_id'])
            
    valid_txs = committed_txs - aborted_txs
    
    for log in wal_logs:
        if log['type'] == 'SET' and log['tx_id'] in valid_txs:
            state[log['key']] = log['value']
            
    return state
