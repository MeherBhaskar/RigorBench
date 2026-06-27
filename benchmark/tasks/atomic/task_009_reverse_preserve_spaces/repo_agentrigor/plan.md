# Plan for `reverse_preserve_spaces`

1.  **Extract non-space characters:** Iterate through the input string `s` and collect all characters that are not spaces into a list.
2.  **Reverse:** Reverse this list of non-space characters.
3.  **Reconstruct string:** Iterate through the original string `s` again.
    *   If the current character is a space, append a space to the result string.
    *   If the current character is not a space, pop the next character from the reversed list of non-space characters and append it to the result string.
4.  **Return:** Return the reconstructed result string.
