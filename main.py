"""
python program
A simple sudoku solver that has
morethan one solution using
Bactracking algortihm
@written by:Mowli
@Date      :16/03/2022
"""

import numpy as np

#sudoku that has more than one solution
box =[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0]
]
#convert this list into matrix
print(print(np.matrix(box)))

#create function to find possible solutions of puzzle
def possibilty(row,column,number):
    global box
    #Check if the number is in same row
    for i in range(0,9):
        if box[row][i] == number:
            return False
    # check if the number is in same column
    for i in range(0,9):
        if box[i][column] == number:
            return False
    #Check if the number is in same square
    x = (column // 3) * 3
    y = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if box[y+i][x+j] == number:
                return False

    return True

#create function to solve puzzle using backtracking algorithm
def solve():
    global box
    for row in range(0,9):
        for column in range(0,9):
            if box[row][column] == 0:
                for number in range(1,10):
                    if possibilty(row,column,number):
                        box[row][column] = number
                        solve()
                        box[row][column] = 0

                return
    #simple design to separate solution
    print("-----------------------")
    print(print(np.matrix(box)))
    # simple design to separate solution
    print("-----------------------")

solve()

