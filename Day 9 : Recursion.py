#---------------------------@AbhijeetK1N6--------------------
"""
Function Description:
Complete the factorial function in the editor below. Be sure to use recursion.

factorial has the following paramter:
int n: an integer

Returns:
int: the factorial of 
"""

# You can use any of the function given below;
##########################################################
#-------------------(Function Type : 1)-------------------
def factorial(n):
    #return math.factorial(n)
    # Write your code here
    if n==1:
        return 1
    else:
        k= n * factorial(n-1)
        return k
#--------------------------------------------------------
##########################################################
#----------------(Function Type : 2)-----------------------
def factorial(n):
    return math.factorial(n)
#---------------------------------------------------------
#############################################################
#---------------(Function Type : 3)-----------------------
def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num
#---------------------------------------------------------
#########################################################
