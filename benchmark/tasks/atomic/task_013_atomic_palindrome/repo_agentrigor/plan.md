# Plan

1. **Understand Requirements**:
   - Function signature: `is_palindrome(s: str) -> bool`
   - Ignore non-alphanumeric characters.
   - Treat uppercase and lowercase as equivalent.
   - Empty string or string with no alphanumeric characters returns True.

2. **Implementation Strategy**:
   - Filter the input string to keep only alphanumeric characters and convert to lowercase.
   - Check if the filtered string is equal to its reverse.

3. **Execution Steps**:
   - Create `palindrome.py` containing the `is_palindrome` function.
   - Create `test_palindrome.py` containing pytest test cases for typical, edge cases, and empty/no-alphanumeric string cases.
   - Run the tests to verify correctness.
