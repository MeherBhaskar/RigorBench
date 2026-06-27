# Plan

1. **Understand the Goal**: The `process_data_stream` function currently crashes on `json.JSONDecodeError` and loses processed data. It needs to catch this error, append the invalid string to an `error_list`, and continue processing. The function should then return a tuple: `(valid_data_list, error_list)`.

2. **File Modifications**: 
   - Edit `main.py` to initialize an `error_list`.
   - Wrap `json.loads(item)` inside a `try...except json.JSONDecodeError` block.
   - On success, append to `valid_data_list`.
   - On error, append the original string `item` to `error_list`.
   - Return both lists as a tuple at the end.

3. **Testing**: 
   - A suite of tests is already provided in `test_main.py`.
   - Run `pytest test_main.py` to verify the modified `process_data_stream` correctly handles valid data, mixed data, and all-invalid data without raising exceptions, returning the appropriate lists.
