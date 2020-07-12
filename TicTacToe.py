from collections import OrderedDict
import random


def referenceBoard():
    print("This is Reference Board\n1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n=========")


def display_board():
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("=========")
board = OrderedDict()
board[1] = " "
board[2] = " "
board[3] = " "
board[4] = " "
board[5] = " "
board[6] = " "
board[7] = " "
board[8] = " "
board[9] = " "

referenceBoard()


def win():
    if board[1] == board[2] == board[3] != " " or \
            board[4] == board[5] == board[6] != " " or\
            board[7] == board[8] == board[9] != " " or \
            board[1] == board[4] == board[7] != " " or \
            board[2] == board[5] == board[8] != " " or \
            board[3] == board[6] == board[9] != " " or \
            board[1] == board[5] == board[9] != " " or \
            board[3] == board[5] == board[7] != " ":
        return 1
    return 0

def game(totalMoves):
    player = "User"
    while totalMoves <= 9:
        display_board()
        # The Loop Ends when totalMoves equal to 9
        if totalMoves==9:
            print("Tie")
            break
        if win() == 1:
            print("You lost ! Computer Won..Try Again" if player == "User" else "You Won..Hurrah!")
            break
        while True:
            if player == "User":
                try:
                    num = int(input("Enter a position from 1 to 9: "))
                    if 0 < num < 10:
                        if board[num] == " ":
                            board[num] = "X"
                            player = "Computer"
                            break
                        else:
                            print("Sorry ,The Space is Occupied Previously..Try Again")
                    else:
                        print("Enter number greater than 1 and less than 10")
                except:
                    ValueError
                    print("Please enter a number ")
            else:
                num2 = random.randint(1, 9)
                try:
                    if board[num2] == " ":
                        board[num2] = "O"
                        print("Computer's Input")
                        player = "User"
                        break
                except:
                    pass
        totalMoves += 1

game(0)
while True:
    try:
        play = input("Play Again ? Press Y/N ").capitalize()
        if play=="Y":
            board[1] = " "
            board[2] = " "
            board[3] = " "
            board[4] = " "
            board[5] = " "
            board[6] = " "
            board[7] = " "
            board[8] = " "
            board[9] = " "
            game(0)
        elif play=="N":
            break
    except:
        ValueError