# Plan for Sudoku Board Verification

## Objective
Write a function `verify_sudoku_board` to validate a 9x9 Sudoku board.

## Logic
A valid Sudoku board requires:
1. No duplicate numbers (1-9) in any of the 9 rows.
2. No duplicate numbers (1-9) in any of the 9 columns.
3. No duplicate numbers (1-9) in any of the 9 3x3 subgrids.
4. Empty cells (represented by 0) are ignored for duplication checks.

## Implementation Steps
1. Create a set to track seen numbers for each row, column, and subgrid, or just iterate and check.
2. Iterate through each cell `(r, c)` in the 9x9 board.
3. If the cell's value is 0, skip it.
4. Check if the value is already in the current row, column, or subgrid set.
5. If it is, return `False`.
6. If the iteration completes without returning `False`, return `True`.

## Testing
Run the existing tests in `test_main.py` using `pytest`.
