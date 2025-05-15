#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def list2Hash(arr):
    Hash = {}

    for value in arr:
        if value in Hash:
            Hash[value] += 1
        if value not in Hash:
            Hash[value] = 1
            
    return Hash

def makeAnagram(a, b):
    Ha = list2Hash(a)
    Hb = list2Hash(b)
    Deletions = 0
    
    for key in a:
        if not(key in Hb and Hb[key] >= 1):
            Deletions += 1
        else:
            Hb[key] -= 1
            
    for key in b:
        if not(key in Ha and Ha[key] >= 1):
            Deletions += 1
        else:
            Ha[key] -= 1
            
    return Deletions
    

a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

print(makeAnagram(a,b))