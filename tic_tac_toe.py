def play_game():

    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

    won = False
    winner = None
    num_moves = 0
    options = [1,2,3,4,5,6,7,8,9]

    print "************Welcome to Tic Tac Toe************ \n"

    print "Enter the location of your move when prompted. \n"

    while won is False and num_moves < 9:

        for row in board:
            print row

        board = handle_player_move('x', options, board)

        if detect_horizontal_win(board, 'x') or detect_vertical_win(board, 'x') or detect_diagonal_win(board, 'x'):
            won = True
            winner = 'Player X'
            break

        num_moves += 1

        for row in board:
            print row

        board = handle_player_move('o', options, board)

        if detect_horizontal_win(board, 'o') or detect_vertical_win(board, 'o') or detect_diagonal_win(board, 'o'):
            won = True
            winner = 'Player O'
            break

        num_moves += 1

    print winner + " has won the game."

def handle_player_move(player, options, board):

    board_moves = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                   4: [1, 0], 5: [1, 1], 6: [1, 2],
                   7: [2, 0], 8: [2, 1], 9: [2, 2]}

    while True:
        try:
            move = int(raw_input('Player ' + player.upper() + ' --> '))
        except ValueError:
            print "Please choose a number between 1 and 9."
            continue
        if move not in options:
            print "Please choose a number between 1 and 9."
        else:
            break

    options = options.remove(move)

    coordinate = board_moves[move]
    coord_1, coord_2 = coordinate
    board[coord_1][coord_2] = player

    return board


def detect_horizontal_win(board, player):
    """Determine if the game has been won via a horizontal win."""

    for i in range(len(board)):
        if board[i].count(player) == len(board[i]):
            return True
    return False


def detect_vertical_win(board, player):
    """Determine if the game as been won via a vertical win."""

    i = 0

    for j in range(len(board)):
        if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player:
            return True
    return False


def detect_diagonal_win(board, player):
    """Determine if the game as been won via a diagonal win."""
    # there is probably a better way to do this

    j = 0
    count = 0

    for i in range(len(board)):
        if board[i][j] == player:
            count += 1
        j += 1

    if count != len(board):
        # check the other way
        k = len(board) -1
        counter = 0
        for i in range(len(board)):
            if board[i][k] == player:
                counter += 1
            k -= 1
        return True if counter == len(board) else False
    return True

################################################################################

h_win = [
         [None, None, None],
         [None, None, None],
         ['x', 'x', 'x'],
        ]

v_win = [
         [None, None, 'x'],
         [None, None, 'x'],
         [None, None, 'x'],
        ]

d_win = [
         ['x', None, 'o'],
         [None, 'x', None],
         ['x', None, 'x'],
        ]

play_game()

# print detect_horizontal_win(h_win, 'x')
# print detect_vertical_win(v_win, 'x')
# print detect_diagonal_win(d_win, 'x')