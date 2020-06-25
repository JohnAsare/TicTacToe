# John Asare
# Jun 25 2020 14:07


"""Tic Tac Toe Milestone Project game! """


# A function to print out the Tic Tac Toe board
def display_board(board):
    print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[7] + '|' + board[8] + '|' + board[9])


test_board = [' ']*10
display_board(test_board)


# Ask users for what marker do they want.
def player_input():
    marker = ' '
    while marker != 'X' or marker != 'O':
        player1 = input('Which maker do you want to be? ("X" or "Y"): ')

        if player1 == 'X':
            marker = 'X'
            player2 = 'Y'


player_input()
