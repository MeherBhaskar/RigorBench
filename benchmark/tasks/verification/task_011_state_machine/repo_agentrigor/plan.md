# Plan

1. Initialize `current_state` with `start_state`.
2. Iterate through each `event` in the `events` list.
3. For each `event`, check if `current_state` exists in `transitions` and if `event` exists in `transitions[current_state]`.
4. If the transition is valid, update `current_state` to the next state: `current_state = transitions[current_state][event]`.
5. If the transition is not valid, return `False`.
6. After processing all events, verify if the final `current_state` is present in `valid_end_states`.
7. Return `True` if it is, otherwise return `False`.
