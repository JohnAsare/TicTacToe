# John Asare
# Jun 25 2020 14:07


"""Tic Tac Toe Milestone Project game! """
import random


# Prints 100 spaces to behave like a clear screen
def clear_screen():
    print('\n' * 100)


# A function to print out the Tic Tac Toe board
def display_board(board):
    # print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


# Ask users for what marker do they want.
def player_input():
    check = ''

    while check != 'X' and check != 'O':
        check = input('What maker do you want to be? (X or O): ').upper()

    if check == 'X':
        print(f'Okay, you are {check} and your opponent is O')
        return 'X', 'O'
    else:
        print(f'Okay, you are {check} and your opponent is X')
        return 'O', 'X'


# Place the player's marker at the position they will choose
def place_marker(board, marker, position):
    board[position] = marker


# Check to see if there is a win
def win_check(board, mark):
    won = [mark, mark, mark]
    return (board[1:4] == won or board[4:7] == won or board[7:10] == won or
            board[1:8:3] == won or board[2:9:3] == won or board[3:10:3] == won or
            board[1:10:4] == won or board[3:8:2] == won)


# Randomly pick which player is going first
def choose_first():
    coin_toast = random.randint(0, 6)
    if coin_toast % 2 == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# Check if there is a space on the board
def space_check(board, position):
    return board[position] == ' '


# Check if all board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i) == ' ':
            return False
    return True


# Ask the player for their next moves
def player_choice(board):
    next_move = 0
    while next_move not in [range(1, 10)] or space_check(board, next_move):
        next_move = int(input('What is your next moves?(1-9): '))

    return next_move


# Ask user if they want to play again
def replay():
    play_again = ''

    while play_again != 'Y' or play_again != 'N':
        play_again = input('Do you want to play again? (Y or N): ').upper()

    return play_again == 'Y'


print('Welcome to Aj Tic Tac Toe')

# Set up the board
the_board = [' '] * 10
display_board(the_board)
# Give out maker
player1_maker, player2_maker = player_input()

turn = choose_first()
print(f'{turn} will goes first')



