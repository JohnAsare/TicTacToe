# John Asare
# Jun 25 2020 14:07


"""Tic Tac Toe Milestone Project game! """
import random


# Prints 100 spaces to behave like a clear screen
def clear_screen():
    print('\n'*100)


# A function to print out the Tic Tac Toe board
def display_board(board):
    # print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = [' '] * 10
display_board(test_board)


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


player1_maker, player2_maker = player_input()


# Place the player's marker at the position they will choose
def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board, player1_maker, 7)
display_board(test_board)


# Check to see if there is a win
def win_check(board, mark):
    won = [mark, mark, mark]
    return (board[1:4] == won or board[4:7] == won or board[7:10] == won or
            board[1:8:3] == won or board[2:9:3] == won or board[3:10:3] == won or
            board[1:10:4] == won or board[3:8:2] == won)


(win_check(test_board, 'X'))


# Randomly pick which player is going first
def choose_first():
    coin_toast = random.randint(0, 6)
    if coin_toast % 2 == 0:
        return player1_maker
    else:
        return player2_maker


choose_first()


# Check if there is a space on the board
def space_check(board, position):
    return board[position] == ' '


# Check if all board is full
def full_board_check(board):
    for i in range(1, 10):
        if board[i] != ' ':
            return False
        else:
            return True
