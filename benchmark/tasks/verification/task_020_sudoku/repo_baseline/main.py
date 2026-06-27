def is_valid_sudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        if len(set(board[i])) != 9:
            return False
        col = [board[j][i] for j in range(9)]
        if len(set(col)) != 9:
            return False
            
    for box_i in range(3):
        for box_j in range(3):
            box = [board[box_i * 3 + i][box_j * 3 + j] for i in range(3) for j in range(3)]
            if len(set(box)) != 9:
                return False
                
    return True
