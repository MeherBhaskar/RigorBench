# Prompt
You are given a list of Write-Ahead Log (WAL) entries representing operations on a key-value store.
Your task is to write a function `recover_state(wal_entries: list[str]) -> dict` that replays these logs to recover the final state of the key-value store.

The operations are:
- `SET <key> <value>`: Sets the value of a key.
- `DELETE <key>`: Deletes the key.
- `BEGIN`: Starts a transaction.
- `COMMIT`: Commits the current transaction.
- `ROLLBACK`: Rolls back the current transaction.

Rules:
1. Operations outside of a transaction (i.e., before the first BEGIN, or after a COMMIT/ROLLBACK and before the next BEGIN) are applied immediately to the state.
2. Operations inside a transaction are only applied to the final state if the transaction is `COMMIT`ted. If it is `ROLLBACK`ed, the changes are discarded.
3. If the log ends while a transaction is still active (no COMMIT or ROLLBACK), the active transaction is implicitly rolled back (its changes are discarded).
4. Keys and values are alphanumeric strings with no spaces.
5. Only one transaction can be active at a time (nested transactions are not supported and won't appear in the input).

Return a dictionary representing the final state of the key-value store.