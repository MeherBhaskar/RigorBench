def recover_state(wal_entries: list[str]) -> dict:
    state = {}
    in_transaction = False
    transaction_state = None
    
    for entry in wal_entries:
        parts = entry.split()
        if not parts:
            continue
            
        op = parts[0]
        if op == "BEGIN":
            in_transaction = True
            transaction_state = state.copy()
        elif op == "COMMIT":
            if in_transaction:
                state = transaction_state
                in_transaction = False
                transaction_state = None
        elif op == "ROLLBACK":
            if in_transaction:
                in_transaction = False
                transaction_state = None
        elif op == "SET":
            if len(parts) >= 3:
                key, val = parts[1], parts[2]
                if in_transaction:
                    transaction_state[key] = val
                else:
                    state[key] = val
        elif op == "DELETE":
            if len(parts) >= 2:
                key = parts[1]
                if in_transaction:
                    transaction_state.pop(key, None)
                else:
                    state.pop(key, None)
                    
    return state
