def row_match(board, p):
    for row in board:
        if row == 4*p:
            return True
    return False

def col_match(board, p):
    for i in range(4):
        if board[0][i]+board[1][i]+board[2][i]+board[3][i] == 4*p:
            return True
        return False

def up_cross_match(board, p):
    for i in range(4):
        if board[i][i] != p:
            return False
    return True

def down_cross_match(board, p):
    for i in range(4):
        if board[i][3-i] != p:
            return False
    return True

def contains_char(board, c):
    for i in range(4):
        for j in range(4):
            if board[i][j] == c:
                return True
    return False

def replace_t(board):
    x_board = [row.replace("T", "X") for row in board]
    o_board = [row.replace("T", "O") for row in board]
    return [x_board, o_board]

def main(board):
    if row_match(board, "X"):
        return "X won"
    if row_match(board, "O"):
        return "O won"
    if col_match(board, "X"):
        return "X won"
    if col_match(board, "O"):
        return "O won"
    if up_cross_match(board, "X"):
        return "X won"
    if up_cross_match(board, "O"):
        return "O won"
    if down_cross_match(board, "X"):
        return "X won"
    if down_cross_match(board, "O"):
        return "O won"
    if contains_char(board, "."):
        return "Game has not completed"
    return "Draw"


for i in range(input()):
    board = [raw_input() for xxx in range(4)]
    raw_input()
    i += 1
    if contains_char(board, "T"):
        res = [main(board) for board in replace_t(board)]
        if res[0] == res[1]:
            print "Case #%i:"%i, res[0]
        else:
            if "won" in res[0]: print "Case #%i:"%i, res[0]
            if "won" in res[1]: print "Case #%i:"%i, res[1]
    else:
        print "Case #%i:"%i, main(board)