1.  **Analyze the Requirements**:
    *   Input: `snapshot` (dict), `log` (list of dicts).
    *   Output: A new dictionary representing the recovered state.
    *   Rules:
        *   Apply `'SET'` operations only if the transaction eventually commits (`'COMMIT'`).
        *   Ignore `'SET'` operations for aborted (`'ABORT'`) or incomplete transactions.
        *   Apply committed operations in the exact order they appear in the log.
        *   Do not modify the input `snapshot`.

2.  **Algorithm**:
    *   First pass through the log to identify which transactions commit.
    *   We can create a set of committed transaction IDs `committed_txs`.
    *   Iterate through the `log`:
        *   If `type` is `'COMMIT'`, add `tx_id` to `committed_txs`.
    *   Create a copy of the `snapshot` called `recovered_state`.
    *   Second pass through the log to apply operations:
        *   Iterate through the `log`:
            *   If `type` is `'SET'` and `tx_id` is in `committed_txs`:
                *   Update `recovered_state[entry['key']] = entry['value']`
    *   Return `recovered_state`.

3.  **Implementation**:
    *   Write the `recover_state` function in `main.py`.

4.  **Testing**:
    *   Run tests in `test_main.py` using `pytest` to verify the implementation.
