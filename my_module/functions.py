"""A collection of function for doing my project."""

def printBoard(board):
    """Prints out the current Connect Four board with the chips that have been inserted.
    
    Parameters
    ----------
    board : list
            A 2D list of coordinates. Zeros indicate empty coordinates while X and O represents chips
            from player one and player two.
    
    Returns
    -------
    This function does not return any values. It is used to display the current board.
    """

    
    #Traverse through every coordinate of the board and print its values
    row = len(board)
    for i in range(row):
        col = len(board[i])
        for j in range(col):
            print(board[i][j], end=' ')
        print()
        
    #Print out visuals and instructions for user
    print("--------------")
    print("0|1|2|3|4|5|6")
    print("Enter column to insert chip")
    print()
    
def resetBoard(board):
    """Resets the current Connect Four board to an empty board with all zero coordinates.
    
    Parameters
    ----------
    board : list
            A 2D list of coordinates. Zeros indicate empty coordinates while X and O represents chips
            from player one and player two.
    
    Returns
    -------
    This function does nto return any values. It is used to reset the current board.
    """

    
    #Traverse through every coordinate and set its value to zero
    row = len(board)
    for i in range(row):
        col = len(board[i])
        for j in range(col):
            board[i][j] = 0
                
                
def setBoard(board, y, player):
    """Modifies the current board by modifying coordinates of where the last chip was inserted.
    
    Parameters
    ----------
    board : list
        A 2D list of coordinates. Zeros indicate empty coordinates while X and O represents chips
        from player one and player two.
    y : int
        Column number of where the chip will be inserted
    player : str
        A string that indicates which player just went
    
    Returns
    -------
    The row coordinate of where the chip is inserted.
    """

    
    #Checks if the spot was empty
    empty = False 
    #Lowest row number
    x = 5 
    
    #While still in bounds and not empty
    while(x > -1 and empty == False):
        #If current spot is taken, go up
        if(board[x][y] == "X" or board[x][y] == "O"):
            x -= 1
        #Current spot is empty
        else: empty = True
    
    #Insert the chip
    if(player == "one" and board[x][y] == 0):
        board[x][y] = "O"
    elif(player == "two" and board[x][y] == 0):
        board[x][y] = "X"
    else:
    #If the entire column is full
        print("You tried to put your chip in a full column and it falls out and you feel silly. You wasted your turn.")
        
    #Return the row coordinate the chip was placed
    return x


def score(player1, player2):
    """Prints out the current scores of players one and two and who is in the lead.
    
    Parameters
    ----------
    player1 : int
            The score of player one
    player2 : int
            The score of player two
    
    Returns
    -------
    This function does not return any values. It is used to display the current board.
    """

    #Display scores of both players 
    print()
    print("Player 1:" , player1)
    print("Player 2:" , player2)
    print()
    
    #Display who is in the lead
    if(player1 > player2):
        print("Player 1 is in the lead!")
        
    elif(player2 > player1):
        print("Player 2 is in the lead!")
    else:
        print("Players are tied!")
    
            
def four(board, x, y, player):
    """Checks if the chip that was inserted has four in a row horizontally, vertically, or diagonally.
    
    Parameters
    ----------
    board : list
        A 2D list of coordinates. Zeros indicate empty coordinates while X and O represents chips
        from player one and player two.
    x : int
        The row coordinate
    y : int
        The column coordinate
    player : str
        A string that indicates which player is being checked
        
    Returns
    -------
    True if there was four in a row and false if there wasn't.
    """

    #Checks letter of chip
    chip = ""
    if(player == "one"):
        chip = "O"
    else:
        chip = "X"
    #Keeps track of consecutive chips   
    consecutive = True 
    #Checks if there was four in a row
    win = False 
    #number of consecutive chips
    counter = 1
    
    #original coordinates
    currx = x
    curry = y
    curr = board[x][y]
    
    #Check all chips on the right
    if(curr == chip):
        x = currx
        y = curry+1
        consecutive = True
    else:
        consecutive = False
    
    while(consecutive == True and y < len(board[0])):
        if(board[x][y] == chip):
            counter += 1
            y += 1
        else:
            consecutive = False
    
    #Check all chips on the left
    if(curr == chip):
        x = currx
        y = curry-1
        consecutive = True
    else:
        consecutive = False
    
    while(consecutive == True and y > -1):
        if(board[x][y] == chip):
            counter += 1
            y -= 1
        else:
            consecutive = False
    
    #Check if there was four in a row
    if(counter >= 4):
        print("FOUR IN A ROW")
        return True
        
    else:
        counter = 1
        
    #Check all chips on top
    if(curr == chip):
        x = currx-1
        y = curry
        consecutive = True
    else:
        consecutive = False
    
    while(consecutive == True and x > -1):
        if(board[x][y] == chip):
            counter += 1
            x -= 1
        else:
            consecutive = False
    
    #Check all chips down
    if(curr == chip):
        x = currx+1
        y = curry
        consecutive = True
    else:
        consecutive = False
    
    while(consecutive == True and x < len(board)):
        if(board[x][y] == chip):
            counter += 1
            x += 1
        else:
            consecutive = False
    
    #Check if there was four in a row
    if(counter >= 4):
        print("FOUR IN A ROW")
        return True
    else:
        counter = 1
    
    #Check all chips diagonally up right
    if(curr == chip):
        x = currx-1
        y = curry+1
        consecutive = True
    else:
        consecutive = False
    
    while(consecutive == True and x > -1 and y < len(board[0])):
        if(board[x][y] == chip):
            counter += 1
            x -= 1
            y += 1
        else:
            consecutive = False
    
    #Check all chips diagonally down left
    if(curr == chip):
        x = currx+1
        y = curry-1
        consecutive = True
    else:
        consecutive = False
    
    while(consecutive == True and x < len(board) and y > -1):
        if(board[x][y] == chip):
            counter += 1
            x += 1
            y -= 1
        else:
            consecutive = False
    
    #Check if there was four in a row
    if(counter >= 4):
        print("FOUR IN A ROW")
        return True
    else:
        counter = 1
    
    #Check all chips diagonally up left
    if(curr == chip):
        x = currx-1
        y = curry-1
        consecutive = True
    else:
        consecutive = False
    
    while(consecutive == True and x > -1 and y > -1):
        if(board[x][y] == chip):
            counter += 1
            x -= 1
            y -= 1
        else:
            consecutive = False
    
    #Check all chips diagonally down right
    if(curr == chip):
        x = currx+1
        y = curry+1
        consecutive = True
    else:
        consecutive = False
    
    while(consecutive == True and x < len(board) and y < len(board[0])):
        if(board[x][y] == chip):
            counter += 1
            x += 1
            y += 1
        else:
            consecutive = False
    
    #Check if there was four in a row
    if(counter >= 4):
        print("FOUR IN A ROW")
        return True
    else:
        counter = 1
    return False


