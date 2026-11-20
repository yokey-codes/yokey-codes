# Given an integer n. 
# You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
# *****
# ****
# ***
# **
# *

n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()