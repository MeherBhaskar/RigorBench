# Plan for recover_logs

1. **Understand the Goal**: The function `recover_logs(log_content: str) -> dict` takes a string representing multiple log lines. Some lines might be invalid JSON or missing `event_type` (str) and `value` (int) fields.
2. **Algorithm**:
    - Initialize an empty dictionary `result` to store the sum of values for each `event_type`.
    - Split the `log_content` by newline characters (`\n`).
    - Iterate over each line:
        - Skip empty lines.
        - Try to parse the line as JSON using `json.loads()`.
        - If a `json.JSONDecodeError` is raised, ignore the line and continue.
        - If parsing is successful, check if the resulting object is a dictionary.
        - Check if `event_type` is in the dictionary and its type is `str`.
        - Check if `value` is in the dictionary and its type is `int` (or `float` that is an integer, but let's stick to `isinstance(val, int)` and not a boolean since bool is a subclass of int in Python).
        - If both conditions are met, add the `value` to `result[event_type]`.
    - Return `result`.
3. **Tests**:
    - The task requires tests. We will check `test_main.py` to see if tests are already written, and if so, run them. If not, we will add test cases.
4. **Implementation**:
    - Update `main.py` to implement `recover_logs` according to the algorithm.
5. **Verification**:
    - Run `pytest test_main.py` to verify the logic.
