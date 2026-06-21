# Prompt
Write a function `is_valid_sudoku(board: list[list[str]]) -> bool` that verifies if a fully filled 9x9 Sudoku board is valid.

A valid Sudoku board is valid if:
1. Each row contains the digits 1-9 without repetition.
2. Each column contains the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid contains the digits 1-9 without repetition.

The board will only contain strings of digits "1" through "9". The board is always 9x9 and fully filled.