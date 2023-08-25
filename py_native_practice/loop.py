###********** Print First 10 natural numbers using while loop*****************************************
# i = 1
# while i <= 10:
#     print(i)
#     i = i+1
# print("Done")
# for i in range(1,11):
#     print(i)    
# print("Done")
###********** Print the following pattern*************************************************************
         
# for i in range(1, 6):  # Outer loop for each line
#     for j in range(1, i + 1):  # Inner loop for printing numbers
#         print(j, end=" ")
#     print()

###**********  Calculate the sum of all numbers from 1 to a given number********************************
from functools import reduce
s = 0
n = int(input("enter the first number : "))
range = range(n+1)
x = reduce(lambda s,n:s+n,range)
print(x)
