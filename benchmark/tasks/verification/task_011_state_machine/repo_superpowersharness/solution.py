def verify_sequence(events, transitions, start_state, valid_end_states):
    current_state = start_state
    
    for event in events:
        if current_state in transitions and event in transitions[current_state]:
            current_state = transitions[current_state][event]
        else:
            return False
            
    return current_state in valid_end_states
