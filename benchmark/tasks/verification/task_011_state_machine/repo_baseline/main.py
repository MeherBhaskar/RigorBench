def verify_sequence(events: list[str], transitions: dict[str, dict[str, str]], start_state: str, valid_end_states: set[str]) -> bool:
    current_state = start_state
    for event in events:
        if current_state not in transitions or event not in transitions[current_state]:
            return False
        current_state = transitions[current_state][event]
    
    return current_state in valid_end_states
