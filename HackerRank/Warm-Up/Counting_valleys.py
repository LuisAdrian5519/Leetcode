#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    Sea_level = 0
    Valleys = 0
    for step in path:
        if step == 'U':
            Sea_level+=1
            if Sea_level == 0:
                Valleys+=1
        elif step == 'D':
            Sea_level-=1

            
    return Valleys           