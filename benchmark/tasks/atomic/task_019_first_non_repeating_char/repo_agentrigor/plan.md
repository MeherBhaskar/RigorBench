# Plan

1. Analyze the problem:
   - Input: A string `s`.
   - Output: The first character in `s` that appears exactly once.
   - If no such character exists, return `""`.

2. Implementation approach:
   - Use a dictionary to keep track of the count of each character. Alternatively, use `collections.Counter`.
   - Python 3.7+ dictionaries preserve insertion order. Thus, the order of characters in the string is naturally preserved.
   - Iterate through the string to populate the character counts.
   - Iterate through the string again (or iterate through the dictionary, since order is preserved) to find the first character with a count of 1.
   - Return that character.
   - If loop finishes without returning, return `""`.

3. Tests:
   - Test with basic examples provided in the prompt.
   - Test with an empty string.
   - Test with string where all characters are repeating.
   - Test with strings where the first non-repeating character is at the beginning, middle, and end.
   - Write these tests using `pytest` format in `test_main.py`.

4. Verification:
   - Run tests using `pytest test_main.py` inside the repo directory.
