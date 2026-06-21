# Prompt

You are given a function `parse_logs(log_file_content: str)` that is supposed to parse a string containing one JSON object per line. Currently, it crashes if a line is malformed JSON.

Modify the function so that it recovers from JSON parsing errors. It should skip the malformed lines, count them, and return a tuple: `(list_of_parsed_dicts, number_of_corrupted_lines)`.