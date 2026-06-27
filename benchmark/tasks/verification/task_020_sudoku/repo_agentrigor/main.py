def is_valid_sudoku(board: list[list[str]]) -> bool:
    for row in board:
        if len(set(row)) != 9:
            return False

    for col_idx in range(9):
        col = [board[row_idx][col_idx] for row_idx in range(9)]
        if len(set(col)) != 9:
            return False

    for box_row in range(3):
        for box_col in range(3):
            sub_box = []
            for r in range(3):
                for c in range(3):
                    sub_box.append(board[box_row * 3 + r][box_col * 3 + c])
            if len(set(sub_box)) != 9:
                return False

    return True
