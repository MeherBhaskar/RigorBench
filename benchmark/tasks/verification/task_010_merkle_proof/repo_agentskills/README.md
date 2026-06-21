# Prompt
Implement a function `verify_merkle_proof(leaf, proof, root)` that verifies a Merkle tree inclusion proof.
- `leaf` is the string representing the data element.
- `proof` is a list of tuples `(direction, hash_value)` where `direction` is either 'left' or 'right', representing whether the sibling hash should be concatenated on the left or the right of the current hash.
- `root` is the expected root hash (string).

Use SHA-256 for hashing. When concatenating two strings (hashes or leaves), concatenate them as strings and then hash the result. Return `True` if the computed root matches the provided root, and `False` otherwise.