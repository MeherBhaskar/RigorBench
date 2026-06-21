# Prompt
Implement a function `verify_merkle_proof(target_hash: str, root_hash: str, proof: list[tuple[str, str]]) -> bool` to verify a Merkle tree inclusion proof.

- `target_hash` is the hash of the leaf node.
- `root_hash` is the expected root hash of the Merkle tree.
- `proof` is a list of tuples `(sibling_hash, direction)` representing the path from the leaf to the root. `direction` is either `'left'` or `'right'`, indicating whether the sibling hash should be prepended (left) or appended (right) to the current hash when combining.
- To combine a left hash `L` and a right hash `R`, concatenate them as `L + R`, encode to `utf-8` bytes, and compute the SHA-256 hex digest.
- The function must process the proof sequentially, updating the current hash at each step. If `direction` is `'left'`, the sibling hash is `L` and the current hash is `R`. If `direction` is `'right'`, the current hash is `L` and the sibling hash is `R`.
- Return `True` if the computed root hash matches the `root_hash`, otherwise `False`.