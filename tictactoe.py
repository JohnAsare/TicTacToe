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
    display_board(board)


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


# Ask the player for their move
def player_choice(board):
    move = 0
    while move not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] or not space_check(board, move):
        move = int(input('What is your move?(1-9): '))

    return move


# Ask user if they want to play again
def replay():
    play_again = ''

    while play_again != 'Y' or play_again != 'N':
        play_again = input('Do you want to play again? (Y or N): ').upper()

    return play_again == 'Y'


print('Welcome to Aj Tic Tac Toe')
while True:

    # Set up the board
    the_board = [' '] * 10
    # Assign the maker
    player1_maker, player2_maker = player_input()
    # Randomly pick who goes first
    goes_first = choose_first()
    print(f'{goes_first} aka {player1_maker} will go first')

    # Ask if they are ready to play
    # play_game = ' '
    # while play_game != 'y' or play_game != 'n':
    play_game = input('Ready to play? (Y or N): ').lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # if they say Y, then let player start playing
    while game_on:
        if goes_first == 'Player 1':
            # Display the board
            display_board(the_board)
            # Ask for their move
            pos = player_choice(the_board)
            # Place their maker on the board
            place_marker(the_board, player1_maker, pos)
            # check if they won
            if win_check(the_board, player1_maker):
                display_board(the_board)
                print('You won!')
                game_on = False
            # Check if it is a tie
            elif full_board_check(the_board):
                display_board(the_board)
                print('Its a tie')
                game_on = False
            else:
                goes_first = 'Player 2'

        elif goes_first == 'Player 2':
            # Display the board
            display_board(the_board)
            # Ask for their move
            pos = player_choice(the_board)
            # Place their maker on the board
            place_marker(the_board, player2_maker, pos)
            # check if they won
            if win_check(the_board, player2_maker):
                display_board(the_board)
                print('You won!')
                game_on = False
            # Check if it is a tie
            elif full_board_check(the_board):
                display_board(the_board)
                print('Its a tie')
                game_on = False
            else:
                goes_first = 'Player 1'

    if not replay():
        break
