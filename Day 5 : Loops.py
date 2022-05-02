#-----------------------@AbhijeetK1N6----------------
"""
Objective
In this challenge, we will use loops to do some math. Check out the Tutorial tab to learn more.

Task
Given an integer, n, print its first 10 multiples. Each multiple should be printed on a new line in the form: n x i = result.
"""

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    c=1
    for i in range(1,11):
        print(n,"x",i,"=",i*n)
