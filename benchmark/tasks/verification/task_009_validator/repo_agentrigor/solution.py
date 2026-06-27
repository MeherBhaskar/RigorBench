def is_valid_sudoku(board: list[list[str]]) -> bool:
    """
    Determines if a 9x9 Sudoku board is valid.
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == '.':
                continue
            
            # Check row
            if val in rows[i]:
                return False
            rows[i].add(val)
            
            # Check col
            if val in cols[j]:
                return False
            cols[j].add(val)
            
            # Check box
            box_index = (i // 3) * 3 + (j // 3)
            if val in boxes[box_index]:
                return False
            boxes[box_index].add(val)
            
    return True
