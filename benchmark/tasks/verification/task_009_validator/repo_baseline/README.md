# Prompt

Write a Python function `is_valid_sudoku(board: list[list[str]]) -> bool` that determines if a 9x9 Sudoku board is valid.

The board is represented as a 2D list of strings, where empty cells are represented by `'.'`. A valid Sudoku board must satisfy the following conditions:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.