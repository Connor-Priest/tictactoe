# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randrange


def start_board():
    global current_player
    board = [['' for x in range(3)] for i in range(3)]
    pos = 1
    for row in range(3):
        for column in range(3):
            board[row][column] = pos
            pos += 1

    board[1][1] = 'X'
    current_player = 'O'
    return board


def display_board(board):
    print('+--------' * 3, '+', sep='')
    for row in range(3):
        print('|        ' * 3, '|', sep='')
        for col in range(3):
            print('|   ', str(board[row][col]) + '   ', end='')
        print('|')
        print('|        ' * 3, '|', sep='')
        print('+--------' * 3, '+', sep='')


def enter_move(board):
    move_allowed = False

    while not move_allowed:
        move = input('Enter a move from 1 to 9: ')

        if len(move) != 1 or move <= '0' or move > '9':
            print('That move is not possible, try again')
            continue

        move = int(move) - 10
        row = move // 3
        col = move % 3

        if board[row][col] in ['O', 'X']:
            print('That square is already occupied, try again. ')
            continue

        move_allowed = not move_allowed
        board[row][col] = 'O'


def make_list_of_free_fields(board):
    free_square = []
    for row in range(3):
            for column in range(3):
                if board[row][column] not in ['O', 'X']:
                    free_square.append((row, column))

    return free_square


def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == sign and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return sign

    for column in range(3):
        if board[0][column] == sign and board[0][column] == board[1][column] and board[0][column] == board[2][column]:
            return sign

    if board[0][0] == sign and board[0][0] == board[1][1] and board[1][1] == board[2][2] or board[0][2] == sign and \
            board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return sign

    return None


def draw_move(board):
    free_square = make_list_of_free_fields(board)

    free_square_length = len(free_square)
    if free_square_length > 0:
        random = randrange(free_square_length)
        row, col = free_square[random]
        board[row][col] = 'X'


def play(board):
    free_square = len(make_list_of_free_fields(board))
    global winner
    global current_player

    while free_square != 0:
        display_board(board)

        if current_player == 'O':
            enter_move(board)
        else:
            draw_move(board)

        game_winner = victory_for(board, current_player)

        if game_winner is not None:
            winner = game_winner
            break
        else:
            if current_player == 'O':
                current_player = 'X'
            else:
                current_player = 'O'

        free_square = len(make_list_of_free_fields(board))


def start_game():
    board = start_board()
    play(board)
    display_board(board)

    if winner is not None:
        print('Congratulations, ', winner, ' has won the game!')
    else:
        print('Its a tie!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
