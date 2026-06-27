# Plan for `reverse_letters`

## Objective
Write a function `reverse_letters(s: str) -> str` that reverses the alphabetic characters in a given string while leaving all non-alphabetic characters in their original positions.

## Approach
1. Convert the input string `s` into a list of characters `chars`, because strings in Python are immutable.
2. Use a two-pointer approach:
   - Initialize `left` pointer to 0 (start of string).
   - Initialize `right` pointer to `len(s) - 1` (end of string).
3. Loop while `left < right`:
   - If `chars[left]` is not an alphabetic character (using `.isalpha()`), increment `left`.
   - Else if `chars[right]` is not an alphabetic character, decrement `right`.
   - Else, swap `chars[left]` and `chars[right]`. Then, increment `left` and decrement `right`.
4. Join the `chars` list back into a string and return it.

## Verification
- Test with various inputs including symbols, numbers, upper/lower case letters, and empty strings.
- Run the provided `pytest` suite in `test_main.py` to ensure all edge cases are handled.
