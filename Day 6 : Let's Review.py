#------------------@AbhijeetK1N6------------------

"""
Objective
Today we will expand our knowledge of strings, combining it with what we have already learned about loops.
Check out the Tutorial tab for learning materials and an instructional video.

Task
Given a string, s, of length n that is indexed from 0 to n-1, print its even-indexed and odd-indexed characters as 2 space-separated strings
on a single line (see the Sample below for more detail).
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
for i in range(0,n):
    s=input()
    print(s[0::2]+" "+s[1::2])
    
