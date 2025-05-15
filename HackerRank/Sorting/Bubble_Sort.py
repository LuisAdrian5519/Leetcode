#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    numSwaps = 0
    for  i in range(len(a)):
        for j in range(len(a)-1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwaps += 1
                
    firstElement = a[0]
    lastElement = a[len(a)-1]
    
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {firstElement}")
    print(f"Last Element: {lastElement}")