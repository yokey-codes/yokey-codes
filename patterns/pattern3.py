# Given an integer n. 
# You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
# 1
# 12
# 123
# 1234
# 12345

n=5
for i in range(n):
    for j in range(1,i+2):  #selects the second loop elements, which selects columns
        print(j,end=" ")
    print()