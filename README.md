# Connect Four
# Objective
This project is a terminal based representation of the popular board game Connect Four, coded in Python.

The board is represented by a 2D list of zero coordinates that indicates that the spot is empty.

Two players will play against each other and take turns inserting their own chips, which are labeled "O" (Player One) and "X" (Player Two).

The two players take turn entering which column they want to insert their chip.

Chips can only be placed on the lowest level. If a chip is already placed in the spot, the next chip will be stacked on top.

Once a player has four consecutive chips of the same letter horizontally, vertically, or diagonally, the player wins.

The scores of both players will be printed and a prompt will ask if they want to play again.

If the players type in y or yes, the board will reset and another game will take place, otherwise the game will close.
