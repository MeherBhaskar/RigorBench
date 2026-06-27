def recover_system(current_state: dict, undo_log: list[str]) -> dict:
    state = current_state.copy()
    for log in reversed(undo_log):
        parts = log.split(" ", 2)
        op = parts[0]
        filename = parts[1]
        
        if op == "CREATE":
            if filename in state:
                del state[filename]
        elif op == "UPDATE":
            state[filename] = parts[2]
        elif op == "DELETE":
            state[filename] = parts[2]
            
    return state
