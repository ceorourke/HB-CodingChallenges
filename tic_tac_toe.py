def print_board():
    """Print a tic tac toe board to the console"""

    print "___"
    print "___"
    print "___"

def play_game():
    """Play the tic tac toe game

    # [   ]
    # [oo ]
    # [xxx]
    """

    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]

    move_x = "x"
    move_o = "o"

    board[2][0] = 'x'
    detect_win(board, move_x)
    board[1][0] = 'o'
    detect_win(board, move_o)
    board[2][1] = 'x'
    detect_win(board, move_x)
    board[1][1] = 'o'
    detect_win(board, move_o)
    board[2][2] = 'x'
    detect_win(board, move_x)


def detect_win(board, player):
    """Determine if a player has won tic tac toe"""

    for row in range(len(board)):
        if (board[row][0] == player) and (board[row][1] == player) and (board[row][2] == player):
            print player + " won" # horizontal win
        elif board[row][0] == player and board[row+1][0] == player and board[row+2][0] == player:
            print player + " won vertically" # vertical win

    # all vertical
    # [0][0], [1][0], [2][0]
    # [0][1], [1][1], [2][1]
    # [0][2], [1][2], [2][2]
    # 2 diagonals
    #[0][0], [1][1], [2][2]
    #[0][2], [1][1], [2][0]


# print_board()
play_game()

