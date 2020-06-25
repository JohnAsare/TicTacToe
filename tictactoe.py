# John Asare
# Jun 25 2020 14:07


"""Tic Tac Toe Milestone Project game! """


# A function to print out the Tic Tac Toe board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[7] + '|' + board[8] + '|' + board[9])


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)
