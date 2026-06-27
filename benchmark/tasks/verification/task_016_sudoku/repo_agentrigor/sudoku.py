def is_valid_sudoku(board: list[list[str]]) -> bool:
    """
    Verifies if a 9x9 Sudoku board is valid.

    Only the filled cells need to be validated according to the following rules:
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    """
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
