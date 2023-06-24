# def hello():
#     return "Sriram Reddy is Student of SR University"
# print(hello())

# def total(a,b):
#     return a+b
#
# a=int(input("Enter the A: "))
# b=int(input("Enter the A: "))
# print(total(a,b))


# def num(n):
#     return n*n*n
# n=int(input())
# print(num(n))

######Lambda Functions
# lambda args : expression

# sum=lambda x,y,z:(x+y+z)
# print(sum(10,2,5))

# num=lambda x,y: if x>y return x else return y
# def small(a,b):
#     if a<b:
#         return a
#     else:
#         return b
# sum=lambda x,y:x+y
# diff = lambda x,y:x-y
# print(small(sum(10,20),diff(20,30)))
# wap to calcuate sum of first 10 natural numbera by using lamba function

# x=lambda:sum(range(1,11))
# print(x())
# fn=input()
# ln=input()
# name=lambda x,y: fn+" "+ln
# print(name(fn,ln))


import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

########win Flags##########
Win = 1
Draw = -1
Running = 0
Stop = 1
###########################
Game = Running
Mark = 'X'


# This Function Draws Game Board
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


# This Function Checks position is empty or not
def CheckPosition(x):
    if (board[x] == ' '):
        return True
    else:
        return False

    # This Function Checks player has won or not


def CheckWin():
    global Game
    # Horizontal winning condition
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
        # Vertical Winning Condition
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
        # Diagonal Winning Condition
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
        # Match Tie or Draw Condition
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running


print("Tic-Tac-Toe Game Designed By Sourabh Somani")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3)
while (Game == Running):
    os.system('cls')
    DrawBoard()
    if (player % 2 != 0):
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark : "))
    if (CheckPosition(choice)):
        board[choice] = Mark
        player += 1
        CheckWin()

os.system('cls')
DrawBoard()
if (Game == Draw):
    print("Game Draw")
elif (Game == Win):
    player -= 1
    if (player % 2 != 0):
        print("Player 1 Won")
    else:
        print("Player 2 Won")












