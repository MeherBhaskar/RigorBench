def recover_system(current_state: dict, undo_log: list[str]) -> dict:
    state = current_state.copy()
    for op in reversed(undo_log):
        parts = op.split(" ", 2)
        action = parts[0]
        filename = parts[1]
        
        if action == "CREATE":
            state.pop(filename, None)
        elif action in ("UPDATE", "DELETE"):
            content = parts[2] if len(parts) > 2 else ""
            state[filename] = content
            
    return state
