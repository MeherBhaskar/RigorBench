def recover_state(wal_entries: list[str]) -> dict:
    state = {}
    in_transaction = False
    pending_ops = []

    for entry in wal_entries:
        parts = entry.strip().split()
        if not parts:
            continue
        
        cmd = parts[0]
        
        if cmd == "BEGIN":
            in_transaction = True
            pending_ops = []
        elif cmd == "COMMIT":
            if in_transaction:
                for op in pending_ops:
                    op_cmd = op[0]
                    if op_cmd == "SET":
                        state[op[1]] = op[2]
                    elif op_cmd == "DELETE":
                        state.pop(op[1], None)
                in_transaction = False
                pending_ops = []
        elif cmd == "ROLLBACK":
            in_transaction = False
            pending_ops = []
        elif cmd == "SET":
            if in_transaction:
                pending_ops.append((cmd, parts[1], parts[2]))
            else:
                state[parts[1]] = parts[2]
        elif cmd == "DELETE":
            if in_transaction:
                pending_ops.append((cmd, parts[1]))
            else:
                state.pop(parts[1], None)
                
    return state
