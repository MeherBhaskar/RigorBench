# Plan for verify_merkle_proof

1. Initialize `current_hash` to the value of `target_hash`.
2. Iterate over the `proof` list, where each element is a tuple `(sibling_hash, direction)`.
3. For each tuple:
   a. If `direction == 'left'`, it means the sibling hash is the left child, and the current hash is the right child. We concatenate them as `sibling_hash + current_hash`.
   b. If `direction == 'right'`, it means the current hash is the left child, and the sibling hash is the right child. We concatenate them as `current_hash + sibling_hash`.
   c. If the direction is invalid (neither 'left' nor 'right'), we can raise a ValueError.
   d. Encode the concatenated string to `utf-8` bytes.
   e. Compute the SHA-256 hash using `hashlib.sha256(encoded_bytes).hexdigest()`.
   f. Update `current_hash` with the new computed hash.
4. After processing the entire proof list, return `current_hash == root_hash`.
