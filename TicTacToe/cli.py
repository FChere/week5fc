# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from typing import List
from logic import make_empty_board, get_winner, other_player

def print_board(board):
    display_board = board
    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                display_board[i][j] = board[i][j]
            else:
                display_board[i][j] = "-"
        print(display_board[i])


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'

    # Show the board to the user
    print_board(board)

    while winner == None:
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.

        # Current player
        print("")
        print(current_player, "please make a move")

        # Input a move from the player
        input_is_valid = False

        while input_is_valid is not True:
            input_x = input("Enter Row: ")
            input_y = input("Enter Col: ")
            coordinate_x = int(input_x) - 1
            coordinate_y = int(input_y) - 1

            if 0 <= coordinate_x <= 2 and 0 <= coordinate_y <= 2:
                input_is_valid = True
            else:
                print("Wrong move, please try again")

        # Update the board
        board[coordinate_x][coordinate_y] = current_player
        print_board(board)

        # Get winner
        winner = get_winner(board)

        # Switch player
        current_player = other_player(current_player)

    print("The winner is", winner)