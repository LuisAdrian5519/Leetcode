import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    
    # Generate a Hash with values and frecuencies
    Hash = {}
    for i in ar:
        if i in Hash:
            Hash[i] += 1
            
        else:
            Hash[i] = 1


    #Count Pairs: Sum of frecuencies / e
    pairs = 0
    for count in Hash.values():
        pairs += count//2

    return pairs


n = 5
ar = [1,2,1,2,3]

print("Número de pares:", sockMerchant(n, ar))