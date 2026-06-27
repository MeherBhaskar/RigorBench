# Plan for Merkle Proof Verification

1. Understand the prompt:
   - Function signature: `verify_merkle_proof(root_hash: str, leaf_hash: str, proof: list) -> bool`
   - `proof` is a list of tuples `(direction, hash_string)`. `direction` is `'left'` or `'right'`.
   - Hashes are hex strings.
   - To compute parent hash: concatenate left and right hex strings, encode to bytes (UTF-8), compute SHA-256 hash. Result is hex digest.
   - Return `True` if computed root matches `root_hash`, else `False`.

2. Implementation Details:
   - Initialize `current_hash` with `leaf_hash`.
   - Iterate through each tuple in `proof`: `(direction, sibling_hash)`.
   - If `direction` is `'left'`, the string to hash is `sibling_hash + current_hash`.
   - If `direction` is `'right'`, the string to hash is `current_hash + sibling_hash`.
   - Compute the SHA-256 hash of the concatenated string (encoded as UTF-8) and obtain the hex digest.
   - Update `current_hash` to this new hex digest.
   - After iterating through all elements in the proof, compare `current_hash` with `root_hash`.

3. Tests:
   - Run the existing tests in `test_main.py` using `pytest`.
   - Add new tests if necessary, but existing ones should cover the requirement.

4. Execution:
   - Edit `main.py` with the implementation.
   - Run tests.
