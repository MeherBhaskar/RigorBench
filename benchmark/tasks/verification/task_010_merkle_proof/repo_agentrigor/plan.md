# Plan

1. Hash the initial leaf string using `hash_node` to obtain the starting hash value.
2. Iterate through each `(direction, hash_value)` in the `proof` list.
3. For each element in the proof:
   - If `direction` is `'left'`, concatenate `hash_value` with the current hash (`hash_value + current_hash`).
   - If `direction` is `'right'`, concatenate the current hash with `hash_value` (`current_hash + hash_value`).
   - Hash the concatenated string using `hash_node` and update the current hash.
4. After processing all elements in the proof, compare the final computed hash with the provided `root`.
5. Return `True` if they match, `False` otherwise.
