# Given an integer n. 
# You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
# 12345
# 1234
# 123
# 12
# 1


n=5
for i in range(n,0,-1): #makes the print upside down
    for j in range(1,i+1): #accesses the elements to print
        print(j,end=" ")
    print()