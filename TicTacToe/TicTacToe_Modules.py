import numpy as np
        
def CheckWin(Grid,Token):
    #Checks for whether columns or rows are completly X or O
    for i in range(3):
        if np.all(Grid[i, :] == Token) or np.all(Grid[:, i] == Token):
            return True
    #Checks for whether diagonals are completely X or O
    if all(np.diag(Grid) == Token) or all(np.diag(np.fliplr(Grid))):
        return True
    return False

def PlaceToken(Grid,Token,x,y):
    Grid[int(x),int(y)] = Token
    Winner = CheckWin(Grid,Token)
    return Winner,Grid
    