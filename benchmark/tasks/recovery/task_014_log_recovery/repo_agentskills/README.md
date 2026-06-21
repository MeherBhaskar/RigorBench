# Prompt
You are tasked with writing a function to recover a filesystem's state after a crash.
You are given a `current_state` dictionary mapping filenames to their string contents, and an `undo_log` which is a list of strings representing operations that were started but need to be rolled back to restore consistency.

The operations in `undo_log` are formatted as follows:
- `CREATE <filename>`: The file was created, so undoing it means removing it.
- `UPDATE <filename> <old_content>`: The file was updated, so undoing it means restoring the `<old_content>`.
- `DELETE <filename> <old_content>`: The file was deleted, so undoing it means recreating it with `<old_content>`.

Note that `<old_content>` can contain spaces.

You must apply the undo operations in reverse order (from the end of the list to the beginning) and return a new dictionary representing the fully recovered state. Do not mutate the original `current_state` dictionary.