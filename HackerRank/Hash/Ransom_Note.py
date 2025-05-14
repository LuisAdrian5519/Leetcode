#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def list2Hash(arr):
    Hash = {}

    for value in arr:
        if value in Hash:
            Hash[value] += 1
        if value not in Hash:
            Hash[value] = 1
            
    return Hash
        

def checkMagazine(magazine, note):
    H_magazine = list2Hash(magazine)
    
    for word in note:
        
        if word in H_magazine and H_magazine[word] > 0:
            H_magazine[word] -=1
        else:
            return print('No')
            
    return print('Yes')


magazine = ["two", "times", "three", "is", "not", "four"]
note = ["two", "times", "two", "is",  "four"]

print(checkMagazine(magazine,note))