# Plan

1. **Understand the Goal**: The objective is to implement a `verify_merkle_proof` function in `main.py` that checks if a given `target_leaf` and a `proof` array evaluates to the `root` hash of a Merkle tree.
2. **Analysis**:
    - Start with `current_hash = target_leaf`.
    - Iterate over `proof`, which is a list of tuples `(direction, sibling_hash)`.
    - If `direction` is `'left'`, concatenate the `sibling_hash` to the left of `current_hash` and compute the hash using `hash_node(sibling_hash, current_hash)`.
    - If `direction` is `'right'`, concatenate the `sibling_hash` to the right of `current_hash` and compute the hash using `hash_node(current_hash, sibling_hash)`.
    - Compare the final `current_hash` with the expected `root` hash. Return `True` if they match, `False` otherwise.
3. **Implementation**: Modify `main.py` using `replace_file_content`.
4. **Testing**: Run tests defined in `test_main.py` using `run_command` with `pytest test_main.py`. Ensure all tests pass.
