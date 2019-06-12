"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import *

##
##

#check for four in a row vertically
def vertical():
    board = [["X", 0, 0, 0, 0, 0, 0],["X", 0, 0, 0, 0, 0, 0],["X", 0, 0, 0, 0, 0, 0],["X", 0, 0, 0, 0, 0, 0],
             ["X", 0, 0, 0, 0, 0, 0],["X", 0, 0, 0, 0, 0, 0]]
    assert four(board, 0,0, "two") == True

    
#check for four in a row horizontally
def horizontal():
    board = [["X", "X", "X", "X", "X", "X", "X"],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
    assert four(board, 0,0, "two") == True

    
#check for four in a row down right    
def downRight():
    board = [["X", 0, 0, 0, 0, 0, 0],[0, "X", 0, 0, 0, 0, 0],[0, 0, "X", 0, 0, 0, 0],[0, 0, 0, "X", 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]] 
    assert four(board, 0,0, "two") == True
    
    
#check for four in a row down left    
def downLeft():
    board = [[0, 0, 0, 0, 0, 0, "X"], [0, 0, 0, 0, 0, "X", 0],[0, 0, 0, 0, "X", 0, 0],[0, 0, 0, "X", 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
    assert four(board, 0,6, "two") == True

    
#check for four in a row up right    
def upRight():
    board = [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, "X", 0, 0, 0],[0, 0, "X", 0, 0, 0, 0],
             [0, "X", 0, 0, 0, 0, 0],["X", 0, 0, 0, 0, 0, 0]]
    assert four(board, 5,0, "two") == True

    
#check for four in a row up left    
def upLeft():
    board = [[0, 0, 0, 0, 0, 0, 0] ,[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, "X", 0, 0, 0],[0, 0, 0, 0, "X", 0, 0],
             [0, 0, 0, 0, 0, "X", 0],[0, 0, 0, 0, 0, 0, "X"]]
    assert four(board, 5,6, "two") == True
