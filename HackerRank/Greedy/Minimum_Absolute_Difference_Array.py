#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    
    arr.sort()
    low = max(arr)
    
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) < low:
            low = abs(arr[i]-arr[i+1])
                
    return low