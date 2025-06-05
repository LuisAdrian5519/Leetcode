#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def str2set(arr):
    cSet = set()
    for i in arr:
        cSet.add(i)
        
    return cSet
        

def twoStrings(s1, s2):
    s1Set = str2set(s1)
    s2Set = str2set(s2)
    
    for char in s1Set:
        if char in s2Set:
            return "YES"
    
    return "NO"