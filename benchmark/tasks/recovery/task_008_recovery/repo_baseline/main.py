def recover_state(wal_entries: list[str]) -> dict:
    state = {}
    transaction_state = None

    for entry in wal_entries:
        parts = entry.split()
        if not parts:
            continue
        cmd = parts[0]

        if cmd == "BEGIN":
            transaction_state = state.copy()
        elif cmd == "COMMIT":
            if transaction_state is not None:
                state = transaction_state
                transaction_state = None
        elif cmd == "ROLLBACK":
            transaction_state = None
        elif cmd == "SET":
            k, v = parts[1], parts[2]
            if transaction_state is not None:
                transaction_state[k] = v
            else:
                state[k] = v
        elif cmd == "DELETE":
            k = parts[1]
            if transaction_state is not None:
                if k in transaction_state:
                    del transaction_state[k]
            else:
                if k in state:
                    del state[k]

    return state
