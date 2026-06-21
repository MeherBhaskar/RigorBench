# Prompt

You are given a multiline string representing a log file where each line is expected to be a valid JSON object. However, the file has been corrupted, and some lines contain malformed JSON or random garbage.

Your task is to write a function `recover_log_data(log_content: str) -> Tuple[List[Dict[str, Any]], int]` that recovers the valid data.

The function should return a tuple containing two items:
1. A list of the successfully parsed JSON objects, in the order they appeared.
2. The number of corrupted lines encountered.

Note:
- Lines that are completely empty or contain only whitespace should be entirely ignored (they are neither valid data nor counted as corrupted lines).
- Any line containing non-whitespace characters that cannot be parsed as a JSON, or parses into something other than a dictionary (e.g., a valid JSON integer like `123` or list like `[1, 2]`), should be counted as a corrupted line.