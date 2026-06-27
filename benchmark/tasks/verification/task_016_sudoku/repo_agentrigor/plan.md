# Plan for Sudoku Validator

## 1. Analyze the Requirements
*   **Input:** `board` - a 9x9 list of lists of strings, representing the Sudoku board. Cells contain either a digit '1'-'9' or '.' for an empty cell.
*   **Output:** `bool` - `True` if valid, `False` otherwise.
*   **Validity Rules:**
    1.  Each row must contain digits 1-9 without repetition.
    2.  Each column must contain digits 1-9 without repetition.
    3.  Each 3x3 sub-box must contain digits 1-9 without repetition.
*   **Note:** Empty cells do not need to be validated. A partially filled board can be valid.

## 2. Implementation Strategy
*   Iterate over each cell in the 9x9 grid, using row index `r` and column index `c`.
*   If the cell at `board[r][c]` is '.', skip it.
*   Track seen values using hash sets for O(1) lookups.
*   Maintain 9 sets for rows, 9 sets for columns, and 9 sets for the 3x3 boxes.
*   The index for the 3x3 box can be calculated using `(r // 3) * 3 + (c // 3)`.
*   For each non-empty cell:
    *   Check if its value exists in the corresponding row set, column set, or box set.
    *   If it does, the board is invalid; return `False`.
    *   If not, add the value to the corresponding row, column, and box sets.
*   If all cells are checked and no duplicates are found, return `True`.

## 3. Code Structure (`sudoku.py`)
```python
def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            
            box_idx = (r // 3) * 3 + (c // 3)
            
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False
                
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
            
    return True
```

## 4. Testing Strategy (`test_sudoku.py`)
Use `pytest` to verify the function against various cases:
1.  Valid completely filled board.
2.  Valid partially filled board.
3.  Invalid board: Duplicate in a row.
4.  Invalid board: Duplicate in a column.
5.  Invalid board: Duplicate in a 3x3 sub-box.
6.  Empty board (all '.').

## 5. Execution Steps
1.  Save this plan in `plan.md`.
2.  Create `sudoku.py` with the implementation.
3.  Create `test_sudoku.py` with the tests.
4.  Run tests using `pytest` to ensure correctness.
