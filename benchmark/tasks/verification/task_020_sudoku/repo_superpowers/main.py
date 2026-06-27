def is_valid_sudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        if len(set(board[i])) != 9:
            return False
            
    for j in range(9):
        col = [board[i][j] for i in range(9)]
        if len(set(col)) != 9:
            return False
            
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(box)) != 9:
                return False
                
    return True
