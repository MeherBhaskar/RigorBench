# Verification Plan: Sudoku Board Validator

## Objective
Implement and verify a Sudoku board validator that checks the validity of a given 9x9 board configuration according to Sudoku rules.

## Sudoku Rules
A Sudoku board is valid if:
1. Each row contains no duplicate numbers from 1 to 9 (ignoring 0/empty cells).
2. Each column contains no duplicate numbers from 1 to 9 (ignoring 0/empty cells).
3. Each of the 9 disjoint 3x3 subgrids contains no duplicate numbers from 1 to 9 (ignoring 0/empty cells).
4. Row and column lengths must be exactly 9.

## Strategy
1. **Validation Checks**:
   - Check dimension constraints: input must be a 9x9 list of lists.
   - For each row, filter out zeroes (empty cells) and ensure all remaining digits are within `[1, 9]` and unique.
   - For each column, apply the same filter and uniqueness check.
   - For each of the nine 3x3 subgrids, check that all non-zero elements are unique.
2. **Implementation details**:
   - The implementation is located in `verify_sudoku_board.py`.
3. **Verification**:
   - Create a test file `test_verify_sudoku_board.py` with:
     - Valid boards.
     - Boards with invalid rows.
     - Boards with invalid columns.
     - Boards with invalid subgrids.
     - Edge cases (boards containing invalid bounds e.g. numbers < 1 or > 9).
     - Dimension mismatch edge cases (non-9x9 boards).
   - Run the tests using `poetry run pytest` and verify success.
