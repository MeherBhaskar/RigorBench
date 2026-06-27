def is_valid_sudoku(board: list[list[str]]) -> bool:
    if not isinstance(board, list) or len(board) != 9:
        return False

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    valid_digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    for r in range(9):
        row = board[r]
        if not isinstance(row, list) or len(row) != 9:
            return False
        for c in range(9):
            val = row[c]
            if not isinstance(val, str):
                return False
            if val == '.':
                continue
            if val not in valid_digits:
                return False
            
            box_index = (r // 3) * 3 + c // 3

            if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                return False
            
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_index].add(val)
            
    return True

