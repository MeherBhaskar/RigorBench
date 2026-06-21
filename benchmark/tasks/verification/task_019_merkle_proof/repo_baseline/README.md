# Prompt
Implement a function `verify_merkle_proof(root, target_leaf, proof)` that verifies a Merkle tree proof.

`proof` is a list of tuples `(direction, hash_value)` where `direction` is either `'left'` or `'right'`, indicating whether the `hash_value` provided in the proof should be concatenated to the left or right of the current computed hash to form the parent node's hash.

A helper function `hash_node(left, right)` is provided, which concatenates the two string inputs and returns their SHA-256 hex digest.

Return `True` if the computed root matches the provided `root` argument, otherwise return `False`.