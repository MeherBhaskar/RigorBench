# Prompt

You are tasked with implementing a data recovery mechanism for a simple in-memory key-value store. The store uses an append-only log to persist operations. Unfortunately, the log file has been corrupted, and some entries are invalid.

Write a function `recover_data(log_lines: list[str]) -> dict[str, str]` that takes a list of log entries and reconstructs the correct state of the key-value store.

Valid operations consist of strictly space-separated tokens:
- `SET <key> <value>` (exactly 3 tokens): Sets the `<key>` to `<value>`.
- `DEL <key>` (exactly 2 tokens): Deletes the `<key>`. If the key doesn't exist, ignore the command.

Any line that does not adhere strictly to these formats is considered corrupted and must be completely ignored. Keys and values will not contain spaces.