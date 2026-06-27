def is_valid_sudoku(board: list[list[str]]) -> bool:
    for row in board:
        if len(set(row)) != 9:
            return False

    for col in range(9):
        col_vals = [board[row][col] for row in range(9)]
        if len(set(col_vals)) != 9:
            return False

    for r_start in range(0, 9, 3):
        for c_start in range(0, 9, 3):
            box_vals = []
            for r in range(3):
                for c in range(3):
                    box_vals.append(board[r_start + r][c_start + c])
            if len(set(box_vals)) != 9:
                return False

    return True
