from main import is_valid_sudoku

def test_valid_sudoku():
    board = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku(board) is True

def test_invalid_sudoku():
    board = [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku(board) is False

def test_empty_board():
    board = [["."] * 9 for _ in range(9)]
    assert is_valid_sudoku(board) is True

def test_invalid_dimensions():
    # Board with less than 9 rows
    board_short = [["."] * 9 for _ in range(8)]
    assert is_valid_sudoku(board_short) is False

    # Board with more than 9 rows
    board_long = [["."] * 9 for _ in range(10)]
    assert is_valid_sudoku(board_long) is False

    # Row with less than 9 columns
    board_narrow = [["."] * 9 for _ in range(9)]
    board_narrow[3] = ["."] * 8
    assert is_valid_sudoku(board_narrow) is False

    # Row with more than 9 columns
    board_wide = [["."] * 9 for _ in range(9)]
    board_wide[5] = ["."] * 10
    assert is_valid_sudoku(board_wide) is False

    # Not a list
    assert is_valid_sudoku(None) is False
    assert is_valid_sudoku("not a board") is False

def test_invalid_types_in_board():
    # Ints instead of strings
    board_ints = [[5 if i == 0 and j == 0 else '.' for j in range(9)] for i in range(9)]
    assert is_valid_sudoku(board_ints) is False

def test_invalid_characters():
    # Digit '0'
    board_zero = [["."] * 9 for _ in range(9)]
    board_zero[0][0] = "0"
    assert is_valid_sudoku(board_zero) is False

    # Digit '10'
    board_ten = [["."] * 9 for _ in range(9)]
    board_ten[0][0] = "10"
    assert is_valid_sudoku(board_ten) is False

    # Letter 'a'
    board_letter = [["."] * 9 for _ in range(9)]
    board_letter[0][0] = "a"
    assert is_valid_sudoku(board_letter) is False

def test_row_duplicate():
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "5"
    board[0][8] = "5"
    assert is_valid_sudoku(board) is False

def test_col_duplicate():
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "5"
    board[8][0] = "5"
    assert is_valid_sudoku(board) is False

def test_box_duplicate():
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "5"
    board[2][2] = "5"
    assert is_valid_sudoku(board) is False

