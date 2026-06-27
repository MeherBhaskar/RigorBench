def recover_state(wal_entries: list[str]) -> dict:
    state = {}
    in_transaction = False
    tx_state = {}

    for entry in wal_entries:
        parts = entry.split()
        if not parts:
            continue
        op = parts[0]

        if op == "BEGIN":
            in_transaction = True
            tx_state = {}
        elif op == "COMMIT":
            if in_transaction:
                for k, v in tx_state.items():
                    if v is None:
                        if k in state:
                            del state[k]
                    else:
                        state[k] = v
                in_transaction = False
                tx_state = {}
        elif op == "ROLLBACK":
            in_transaction = False
            tx_state = {}
        elif op == "SET":
            if len(parts) >= 3:
                k, v = parts[1], parts[2]
                if in_transaction:
                    tx_state[k] = v
                else:
                    state[k] = v
        elif op == "DELETE":
            if len(parts) >= 2:
                k = parts[1]
                if in_transaction:
                    tx_state[k] = None
                else:
                    if k in state:
                        del state[k]

    return state
