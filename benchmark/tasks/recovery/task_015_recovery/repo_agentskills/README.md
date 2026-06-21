# Prompt
You are given an initial state of a key-value store (a dictionary) and a write-ahead log (a list of dictionaries). Your task is to implement the `recover_state` function that replays the log to recover the final state of the store.

Each log entry is a dictionary with at least the following keys:
- `tx_id`: an integer uniquely identifying the transaction
- `type`: a string representing the operation type, which can be `'START'`, `'SET'`, `'COMMIT'`, or `'ABORT'`

For `'SET'` operations, the log entry will also contain:
- `key`: the string key being modified
- `value`: the new value for the key

Rules for recovery:
1. You must apply `'SET'` operations to the state only if the transaction they belong to eventually commits (has a `'COMMIT'` log entry).
2. If a transaction has an `'ABORT'` entry, or neither `'COMMIT'` nor `'ABORT'` (an incomplete transaction), its `'SET'` operations must be completely ignored.
3. Operations from committed transactions must be applied in the exact order they appear in the log.
4. You should not modify the input `snapshot` dictionary in place; return a new dictionary with the recovered state.