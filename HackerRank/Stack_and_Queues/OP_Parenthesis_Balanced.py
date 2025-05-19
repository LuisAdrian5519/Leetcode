#!/bin/python3

import math
import os
import random
import re
import sys


def isBalanced(s):
    Balance = []
    matches = {'(':')', '[':']', '{':'}'}
    
    for char in s:
        if char in matches:
            Balance.append(char)
        elif char in matches.values():
            if Balance and Balance[-1] in matches and matches[Balance[-1]] == char:
                Balance.pop()
            else:
                return "NO"
    
    return "YES" if not Balance else "NO"
