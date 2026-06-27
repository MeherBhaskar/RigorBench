def verify_sequence(events: list[str], transitions: dict[str, dict[str, str]], start_state: str, valid_end_states: set[str]) -> bool:
    current_state = start_state
    for event in events:
        state_transitions = transitions.get(current_state)
        if not state_transitions or event not in state_transitions:
            return False
        current_state = state_transitions[event]
    return current_state in valid_end_states
