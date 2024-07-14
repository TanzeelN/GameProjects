def CheckWin(Token,Grid):
    Winner = False
    WinningToken = None
    for i in range(0,3):
        #Winner by row
        if all(Grid[i,:] == Token):
            Winner = True
            WinningToken = Token
            return Winner, WinningToken
            break
        #Winner by column
        elif all(Grid[:,i] == Token):
            Winner = True
            WinningToken = Token
            return Winner, WinningToken
            break
        else:
            Winner = False
            
    Diagonal1 =[(0,0),(1,1),(2,2)]
    Diagonal2 = [(2,0),(1,1),(0,2)]
    
    if Winner == False:
        if Grid[0,0] == Token and Grid[1,1] == Token and Grid[2,2] == Token:
            Winner = True
            WinningToken = Token
            return Winner, WinningToken
        else:
            Winner = False
        
        if Grid[2,0] == Token and Grid[1,1] == Token and Grid[0,2] == Token:
            Winner = True
            WinningToken = Token
            return Winner, WinningToken
        else:
            Winner = False
    else:
        Winner = False
    
    return Winner,WinningToken
        
    