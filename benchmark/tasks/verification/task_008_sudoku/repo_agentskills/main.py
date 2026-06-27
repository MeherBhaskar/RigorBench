def verify_sudoku_board(board: list[list[int]]) -> bool:
    for i in range(9):
        row_seen = set()
        col_seen = set()
        for j in range(9):
            row_val = board[i][j]
            if row_val != 0:
                if row_val in row_seen:
                    return False
                row_seen.add(row_val)
                
            col_val = board[j][i]
            if col_val != 0:
                if col_val in col_seen:
                    return False
                col_seen.add(col_val)
                
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square_seen = set()
            for row in range(3):
                for col in range(3):
                    val = board[i + row][j + col]
                    if val != 0:
                        if val in square_seen:
                            return False
                        square_seen.add(val)
    return True
