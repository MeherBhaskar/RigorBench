def recover_system(current_state: dict, undo_log: list[str]) -> dict:
    state = current_state.copy()
    for operation in reversed(undo_log):
        parts = operation.split(" ", 2)
        action = parts[0]
        filename = parts[1]
        
        if action == "CREATE":
            state.pop(filename, None)
        elif action in ("UPDATE", "DELETE"):
            state[filename] = parts[2]
            
    return state
