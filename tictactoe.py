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
    check = ''

    while check != 'X' or check != 'Y':
        player1 = input('What maker do you want? (X or Y): ')

        if player1 == 'X':
            player2 = 'Y'
            print(f'Opponent is Y')
            break
        elif player1 == 'Y':
            player2 = 'X'
            print(f'Opponent is X')
            break


player_input()
