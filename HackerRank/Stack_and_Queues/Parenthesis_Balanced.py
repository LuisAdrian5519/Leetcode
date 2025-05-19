#!/bin/python3

import math
import os
import random
import re
import sys


def isBalanced(s):
    Balance = []
    
    for char in s:
        if char == '(' or char == '[' or char=='{':
            Balance.append(char)
        elif char == ')':
            if Balance[-1] == '(':
                Balance.pop()
            else:
                return "NO"
        elif char == ']':
            if Balance[-1] == '[':
                Balance.pop()
            else:
                return "NO"
        else:
            if Balance[-1] == '{':
                Balance.pop()
            else:
                return "NO"
    
    return "YES"