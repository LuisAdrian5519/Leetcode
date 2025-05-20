#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def array2Hash(arr):
    Arr_Hash = {}
    for element in arr:
        if element in Arr_Hash:
            Arr_Hash[element]+=1
        else:
            Arr_Hash[element]=1
            
    return Arr_Hash

def repeatedString(s, n):
    Arr_Hash = array2Hash(s)
        
    if 'a' in Arr_Hash:
        Frequency = Arr_Hash['a']*(n//len(s))
    else:
        return 0
        
    for i in range(n%len(s)):
        if s[i] == 'a':
            Frequency+=1
            
    return Frequency