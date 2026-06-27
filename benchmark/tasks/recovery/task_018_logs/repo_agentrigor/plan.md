# Plan to modify `parse_logs`

1. The function needs to return a tuple containing the list of parsed dictionaries and the count of corrupted lines.
2. Initialize `parsed` as an empty list and `corrupted_count` as 0.
3. If `log_file_content.strip()` is empty, return `([], 0)`.
4. Split the input by `\n` and iterate over each line.
5. If the line is not empty (`line.strip()`), try to parse it using `json.loads(line)`.
6. Catch `json.JSONDecodeError`. If parsing is successful, append the parsed object to `parsed`.
7. If a `json.JSONDecodeError` is caught, increment `corrupted_count`.
8. Return `(parsed, corrupted_count)`.
