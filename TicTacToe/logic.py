# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(Board):

    winner = ""

    if Board[0][0] == Board[1][1] == Board[2][2] or Board[0][2] == Board[1][1] == Board[2][0]:

        winner = Board[1][1]

    else:

        for i in range(0,3):

            if Board[i][0] == Board[i][1] == Board[i][2]:

                winner = Board[i][0]

                break

            elif Board[0][i] == Board[1][i] == Board[2][i]:

                winner = Board[0][i]

                break

    if winner == "":

        winner = None

    else:

        print(winner,"Won")

    return winner




def other_player(player):

    if player == 'X':

        return 'O' 

    elif player == 'O':

        return 'X'