from TicTacToe.TicTacToe_Modules import *
import numpy as np


#Setting conditions to initiate the game.
Game = True
Winner = False
Counter = 1
Grid = np.full((3,3),'')

print("To play this game, you have to use coordinates to say where you like to place the token (X or O).")
print("For Example, 1,1 would place the token on the first row & the first column (the top middle spot).")
while Game == True:
    
    x1,y1 = input("Where would you like to place the X?").split(",")
    x1 = int(x1)
    y1 = int(y1)
    Grid[x1-1,y1-1] = 'X'
    Winner,WinningToken = CheckWin('X',Grid)
    if Winner == True:
        print("X has won, Thank you for playing!")
        break
    else:
        None
    
    x1,y1 = input("Where would you like to place the O?").split(",")
    x1 = int(x1)
    y1 = int(y1)
    Grid[x1-1,y1-1] = 'O'
    Winner,WinningToken = CheckWin('O',Grid)
    if Winner == True:
        print("O has won, Thank you for playing!")
        break
    else:
        None
    
        
