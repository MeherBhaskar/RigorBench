# Plan for Log Recovery

## Objective
Implement `recover_system` to restore filesystem state by applying undo operations in reverse order, without mutating the original `current_state` dictionary.

## Approach
1. Create a shallow copy of `current_state` to avoid mutating the original dictionary. This ensures atomic transitions.
2. Iterate through `undo_log` in reverse order using `reversed()`.
3. For each operation string, split it by spaces at most 2 times (i.e., `op.split(" ", 2)`). This will separate the action, the filename, and the potentially space-containing `old_content`.
4. Based on the action:
   - `CREATE`: Use `dict.pop(filename, None)` to remove the file.
   - `UPDATE`: Update the dictionary with `filename` and the extracted `old_content`.
   - `DELETE`: Recreate the file by adding `filename` and `old_content` to the dictionary.
5. Return the newly modified dictionary representing the recovered state.

## Testing
1. Run the existing tests in `test_main.py`.
2. Add any additional tests if necessary (e.g. testing empty files).
3. Verify that all tests pass.
