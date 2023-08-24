#******************1st question**********************Calculate the multiplication and sum of two numbers
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# if num1*num2 <=1000:
#     print("The answers is ", num1*num2)

    
# else:
#     print("The answer is", num1+num2) 
#***********2nd question**********************Print the sum of the current number and the previous number
# previous_num = 0
# for i in range(1,11):
#     sum = previous_num + i
#     print("Current number ", i , "Previous number ", previous_num,"Sum is ", sum)
#     previous_num = i
#***********2nd question********************** or
# str = input("Enter the string : ")  
# for i in range(0,len(str)-1,2):
#     print(str[i])
#***********3rd question**********************Print characters from a string that are present at an even index number
# str = input("Enter the string")  
# for i in str[0::2]:
#     print(i)
#***********4th question**********************Remove first n characters from a string
# def remove_char(word,n):
#     print("original string : ", word)
#     x = word[n: ]
#     return x
# print(remove_char("python",2))
#***********5th question**********************Check if the first and last number of a list is the same
# def given_list(list):
#     if list[0] == list[-1]:    #list[-1] or len(list)-1=n and if list[0] == len(list)-1 can be used
#         return "Result is True"
#     else:
#         return "Result is False"
# x = given_list([10,23,23,1,10])    
# y = given_list([10,23,23,1,11])    
# print(x)
# print(y)
#***********6th question********************** Display numbers divisible by 5 from a list
# list = [10,20,30,40,50,11,22,33,44]
# for i in list:
#     if i%5 !=0:
#         pass
#     else:
#         print(i)

# print("bye")       
# #***********6th question********************** or

# def multiple(list):
#     for i in list:
#         if i % 5 !=0:
#             pass
#         else:
#             print(i)
# multiple([10,20,30,40,50,1,2,3,4])        
#***********6th question********************** or
# list = [10,20,11,22,33,30,40,50,11,22,33,44]
# for i in list:
#     if i%5 ==0:
#         print(i)
#***********7th question**********************  Return the count of a given substring from a string
# str = ("Hello I am s software developer.Hello Hello Hello")
# n = str.count("Hello")
# print("Hello is appeared ", n ," times")
#***********14th question********************** Print downward Half-Pyramid Pattern with Star (asterisk)
# for i in range(5, 0, -1):
#     for j in range(0, i - 1):
#         print("#", end=' ')
#     print(" ")
# #***********14th question********************** 
# for i in range(4):
#     for j in range(4 - i):        #not getting the pattern
#         print("#", end=" ")
# #***********13th question********************** Print multiplication table form 1 to 10
# for i in range(1,11):
#     for j in range (1,11): 
#         print(i*j,end ="  ")  
#     print("\t\t")        
# #***********11th question********************** Write a Program to extract each digit from an integer in the reverse order.
num  = "hello"
reverse = num[::-1]
print(reverse)

nulm = 23456
reverse = nulm[::-1]
print(reverse)

                   



    









         



