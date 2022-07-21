def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def can_place_queen(r, c, rows, cols, left_diag, right_diag):
    if r in rows:
        return False
    if c in cols:
        return False
    if (c - r) in left_diag:
        return False
    if (r + c) in right_diag:
        return False
    return True


def set_queen(r, c, board, rows, cols, left_diag, right_diag):
    board[r][c] = '*'
    rows.add(r)
    cols.add(c)
    left_diag.add(c - r)
    right_diag.add(r + c)


def remove_queen(r, c, board, rows, cols, left_diag, right_diag):
    board[r][c] = '-'
    rows.remove(r)
    cols.remove(c)
    left_diag.remove(c - r)
    right_diag.remove(r + c)


def put_queens(r, board, rows, cols, left_diag, right_diag):
    if r == 8:
        print_board(board)
        return
    for c in range(8):
        if can_place_queen(r, c, rows, cols, left_diag, right_diag):
            set_queen(r, c, board, rows, cols, left_diag, right_diag)
            put_queens(r + 1, board, rows, cols, left_diag, right_diag)
            remove_queen(r, c, board, rows, cols, left_diag, right_diag)


n = 8
board = [['-'] * n for _ in range(n)]

put_queens(0, board, set(), set(), set(), set())