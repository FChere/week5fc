
# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import get_winner

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    turn = 0
    move = 0
    now = None
    
    while winner == None:
        if (turn + 2) % 2 == 0:
            now = 'X'
        else:
            now = 'O'

        print("X: take a turn!")
        print(board[0],'\n',board[1],'\n',board[2],'\n')
        print('[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]')

        move = input("your move (example: 1): ")
        move = int(move)

        if move == 1:
            board[0][0] = now
            print('move = ', move)
        if move == 2:
            board[0][1] = now
            print('move = ', move)
        if move == 3:
            board[0][2] = now
            print('move = ', move)
        if move == 4:
            board[1][0] = now
            print('move = ', move)
        if move == 5:
            board[1][1] = now
            print('move = ', move)
        if move == 6:
            board[1][2] = now
            print('move = ', move)
        if move == 7:
            board[2][0] = now
            print('move = ', move)
        if move == 8:
            board[2][1] = now
            print('move = ', move)
        if move == 9:
            board[2][2] = now
            print('move = ', move)
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        print(board[0],'\n',board[1],'\n',board[2],'\n')

        print('Turn:', turn)
        if turn > 1:
            winner = get_winner(board, turn)
        if winner != None:
            print('winner is: ', winner, '!')
        turn = turn + 1
