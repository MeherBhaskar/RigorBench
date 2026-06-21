# Prompt
You are given a function `process_data_stream(stream)` in `main.py` that processes a list of JSON strings.
Currently, if it encounters an invalid JSON string, it raises a `json.JSONDecodeError` and crashes, losing all processed data up to that point.
Modify the function so that it gracefully recovers from `json.JSONDecodeError`s.
If an invalid JSON string is encountered, catch the exception, append the invalid string to a separate list of errors, and continue processing the rest of the stream.
The function should return a tuple of two lists: `(valid_data_list, error_list)`.