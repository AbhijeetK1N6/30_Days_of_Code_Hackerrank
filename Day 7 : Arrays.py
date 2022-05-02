#---------------@AbhijeetK1N6---------------------

"""
Objective:
Today, we will learn about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video.

Task:
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#--coded by send--
if __name__ == '__main__':
    n=int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    for i in (arr):
        print(i,end=" ")
