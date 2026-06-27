# Plan for `recover_jsonl_data`

1. **Objective**: Implement a function `recover_jsonl_data(filepath: str) -> list[dict]` that reads a JSONL file, parses each line as JSON, ignores lines that fail to parse, and returns a list of valid JSON objects.
2. **Location**: The implementation and tests will be in `/home/meher/dev/rigorbench-paper/benchmark/tasks/recovery/task_007_recovery/repo_agentrigor`.
3. **Implementation Details**:
   - Import `json`.
   - Open the file at `filepath`.
   - Iterate through the file line by line.
   - For each line, strip whitespace and attempt to `json.loads(line)`.
   - If a `json.JSONDecodeError` occurs, catch it and ignore the line.
   - If parsing succeeds, append the resulting dictionary to a list.
   - Return the list.
4. **Testing**:
   - Write tests using `pytest` or `unittest`.
   - Create a temporary file with a mix of valid JSON objects, empty lines, and completely invalid JSON.
5. **Execution**:
   - Create `solution.py` and `test_solution.py`.
   - Run tests.
