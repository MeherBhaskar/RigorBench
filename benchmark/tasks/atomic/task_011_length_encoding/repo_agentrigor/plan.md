# Plan for Run-Length Encoding

1.  **Understand the Goal**: Create a function `run_length_encode(text)` that performs run-length encoding. For example, "AABBCCCA" -> "2A2B3C1A". Empty string returns empty string.
2.  **Implementation Details**:
    *   Initialize an empty result list or string.
    *   Handle edge case: if `text` is empty, return "".
    *   Keep track of the current character and its count.
    *   Iterate through the string:
        *   If the current character is the same as the previous one, increment the count.
        *   If it's different, append the count and previous character to the result, reset count to 1, and update the current character.
    *   After the loop, append the final count and character.
    *   Join and return the result.
3.  **Testing**:
    *   Write tests using `unittest` or `pytest`.
    *   Test cases: empty string, single character, all same characters, all different characters, mixed characters.
4.  **Verification**: Run the tests to ensure correctness.
