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
    
    # Verificar las diferencias en las frecuencias
    for key in Ha:
        if key in Hb:
            deletions += abs(Ha[key] - Hb[key])
        else:
            deletions += Ha[key]
    
    # Verificar las letras que están solo en Hb
    for key in Hb:
        if key not in Ha:
            deletions += Hb[key]
            
    return deletions
    

a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

print(makeAnagram(a,b))