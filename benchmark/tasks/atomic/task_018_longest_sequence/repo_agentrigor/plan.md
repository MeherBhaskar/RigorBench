# Plan

1. Check for the empty string edge case. If `s` is empty, return `("", 0)`.
2. Initialize variables `max_char = ""` and `max_len = 0` to store the character with the longest sequence and its length.
3. Initialize `current_char = s[0]` and `current_len = 1` to track the current sequence being examined.
4. Iterate through the string `s` starting from the second character (index 1).
   - If the current character matches `current_char`, increment `current_len`.
   - If the current character is different from `current_char`:
     - Check if `current_len > max_len`. If it is, update `max_char = current_char` and `max_len = current_len`.
     - Reset `current_char` to the new character and `current_len = 1`.
5. After the loop completes, perform one final check to see if the last sequence examined is the longest (`if current_len > max_len: max_char = current_char; max_len = current_len`).
6. Return a tuple `(max_char, max_len)`.
