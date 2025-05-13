#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def sumD(arr, row,col):
    return (
        arr[row][col] + arr[row][col+1] + arr[row][col+2] +
        arr[row+1][col+1] +
        arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
    )

def hourglassSum(arr):

    HG_Sums = []
    
    for row in range(4):
        for value in range(4):
            HG_Sums.append(sumD(arr, row,value))

    return max(HG_Sums)
    

arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

print(hourglassSum(arr))