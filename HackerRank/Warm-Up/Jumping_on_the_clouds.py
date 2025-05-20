#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    jumps = 0
    position = 0
    while position < len(c)-1:
        if position + 1 == len(c)-1:
            return jumps + 1
        elif c[position + 2] == 1:
            position+=1
            jumps+=1
        else:
            position+=2
            jumps+=1
            
    return jumps
