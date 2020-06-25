# John Asare
# Jun 25 2020 14:07


"""Tic Tac Toe Milestone Project game! """


# A function to print out the Tic Tac Toe board
def display_board(board):
    #print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = [' ']*10
display_board(test_board)


# Ask users for what marker do they want.
def player_input():
    check = ''

    while check != 'X' and check != 'O':
        check = input('What maker do you want to be? (X or O): ')

    player1 = check
    if player1 == 'X':
        print('Opponent is O')
        player2 = 'O'
    else:
        print('Opponent is X')
        player2 = 'X'
    return player1, player2


player1_maker, player2_maker = player_input()


# def place_marker(board, marker, position):
#
#
#
# place_marker(test_board,'$',8)
# display_board(test_board)


