# Plan for Validating a Sudoku Board

## Objective
Implement `is_valid_sudoku(board: list[list[str]]) -> bool` to determine if a partially filled 9x9 Sudoku board is valid according to the standard rules.

## Constraints & Rules
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each 3x3 sub-box must contain the digits `1-9` without repetition.
4. Empty cells are represented by `'.'`.
5. Only filled cells need to be validated.

## Approach
1. Iterate over the board cell by cell (nested loops: `i` for rows `0..8`, `j` for columns `0..8`).
2. Use a set or boolean array to track seen numbers for:
   - Each row (9 sets)
   - Each column (9 sets)
   - Each 3x3 box (9 sets, indexed by `(i // 3) * 3 + (j // 3)`).
3. As we encounter a filled cell (not `'.'`):
   - Check if the number is already in the corresponding row set, column set, or box set.
   - If it is, the board is invalid (return `False`).
   - If not, add the number to the corresponding row, column, and box sets.
4. If we successfully check all cells without conflicts, return `True`.

## Implementation Steps
1. Create `solution.py` with the `is_valid_sudoku` function.
2. Create `test_solution.py` with pytest test cases covering various valid and invalid scenarios.
3. Run the tests to verify the implementation.
