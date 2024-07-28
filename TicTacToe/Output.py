from TicTacToe.TicTacToe_Modules import *
import numpy as np

'''Things that have been added:
- Added a function Place Token which also checks if someone has won.
- Cleaned the code to make it more readable
'''


#Setting conditions to initiate the game.
Game = True
Winner = False
Grid = np.full((3,3),'')


print("To play this game, you have to use coordinates to say where you like to place the token (X or O).")
while Game == True:
    
    x,y = input("Where would you like to place the X?").split(",")
    Winner,Grid = PlaceToken(Grid,'X',x,y)
    if Winner == True:
        print("X has won, Thank you for playing!")
        break
  
    x,y = input("Where would you like to place the O?").split(",")
    Winner,Grid = PlaceToken(Grid,'O',x,y)
    if Winner == True:
        print("O has won, Thank you for playing!")
        break
    
    
        
