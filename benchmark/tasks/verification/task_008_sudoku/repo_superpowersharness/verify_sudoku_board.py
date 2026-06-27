def verify_sudoku_board(board: list[list[int]]) -> bool:
    if len(board) != 9:
        return False
    
    for row in board:
        if len(row) != 9:
            return False

    # Check rows
    for row in board:
        seen = set()
        for num in row:
            if num != 0:
                if num in seen or num < 1 or num > 9:
                    return False
                seen.add(num)

    # Check columns
    for col in range(9):
        seen = set()
        for row in range(9):
            num = board[row][col]
            if num != 0:
                if num in seen or num < 1 or num > 9:
                    return False
                seen.add(num)

    # Check 3x3 grids
    for i in range(3):
        for j in range(3):
            seen = set()
            for row in range(i * 3, i * 3 + 3):
                for col in range(j * 3, j * 3 + 3):
                    num = board[row][col]
                    if num != 0:
                        if num in seen or num < 1 or num > 9:
                            return False
                        seen.add(num)

    return True
