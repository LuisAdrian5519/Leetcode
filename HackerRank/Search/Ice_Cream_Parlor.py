#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    
    hashmap = {}    
    for i in range(len(cost)):
        incognito = money - cost[i]
        if incognito in hashmap:
            print(f"{hashmap[incognito]+1} {i+1}")
            return
        hashmap[cost[i]] = i


cost = [1, 4, 5, 3, 2]
money = 4

whatFlavors(cost, money)

