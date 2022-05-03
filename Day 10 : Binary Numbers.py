#--------------------@AbhijeetK1N6----------------------
"""
Task
Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
When working with different bases, it is common to show the base as a subscript.
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    bcd = []
    
    while n > 0:
        bc = n % 2
        n = n//2
        bcd.append(bc)
    
    c,result = 0,0
    
    for i in range(0,len(bcd)):
        if bcd[i] == 0:
            c = 0
        else:
            c +=1
            result = max(result,c)
    
    print(result)
