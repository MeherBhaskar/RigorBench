# Plan
1.  **Analyze the Requirements**:
    *   Input: A string `s`.
    *   Output: A boolean indicating whether `s` is a palindrome.
    *   Conditions:
        *   Ignore case (convert all to lowercase or uppercase).
        *   Only consider alphanumeric characters.

2.  **Implementation Strategy**:
    *   Filter the input string `s` to keep only alphanumeric characters and convert them to lowercase.
    *   Compare the filtered string with its reverse.
    *   Return `True` if they are equal, `False` otherwise.

3.  **Testing**:
    *   The existing `test_main.py` already has relevant test cases.
    *   I will run `pytest` to ensure the implementation is correct.
