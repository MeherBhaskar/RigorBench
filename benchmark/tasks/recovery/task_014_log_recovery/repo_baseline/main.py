def recover_system(current_state: dict, undo_log: list[str]) -> dict:
    state = current_state.copy()
    for entry in reversed(undo_log):
        parts = entry.split(" ", 2)
        op = parts[0]
        filename = parts[1]
        
        if op == "CREATE":
            if filename in state:
                del state[filename]
        elif op in ("UPDATE", "DELETE"):
            old_content = parts[2] if len(parts) > 2 else ""
            state[filename] = old_content
            
    return state
