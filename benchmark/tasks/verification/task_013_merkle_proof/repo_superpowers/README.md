# Prompt

Implement a function `verify_merkle_proof(root_hash: str, leaf_hash: str, proof: list) -> bool` that verifies a Merkle tree proof. 

In this system, a Merkle tree is constructed using SHA-256 hashing. The `proof` is a list of tuples `(direction, hash_string)`. 
- `direction` is either `'left'` or `'right'`, indicating whether the sibling `hash_string` should be concatenated to the left or right of the current hash.
- Hashes are represented as hex strings.
- To compute the parent hash, concatenate the left and right hex strings, encode the concatenated string to bytes using UTF-8, and compute the SHA-256 hash. The result should be the hex digest.

Return `True` if the computed root hash matches the provided `root_hash`, and `False` otherwise.