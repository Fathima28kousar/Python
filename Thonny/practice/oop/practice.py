'''f = open("one.txt","r")
lines = f.readlines()
f.close()
fp = open("new_file.txt","w")
count = 0
for line in lines:
    if count ==4:
        count+=1
        continue
    else:
        fp.write(line)
        count+=1
fp.close()        
'''
'''
import random
heading = "newhorizon"
print(random.choice(heading))'''

'''import secrets
sectretsGenerator = secrets.SystemRandom()
print("Generating 4-digit random otp")
otp = sectretsGenerator.randrange(1000,9999)
print("Secure random otp is ",otp)

import secrets
secretsGenerator = secrets.SystemRandom()
otp = secretsGenerator.randrange(100,999)
print("otp is ",otp)

import secrets
secretsGenrator = secrets.SystemRandom()
otp = secretsGenerator.randrange(100,999)
print("otp is ",otp)'''

'''import random
list = []
for i in range(100):
    list.append(random.randrange(10000,99999))
winners = random.sample(list,20)
print(winners)    
'''

'''import random
for i in range(3):
    print(random.randrange(100,999,4),end=" ")'''
'''
c = 0
num = int(input("enter the no."))
if num>1:
    for i in range(2,(int(num/2)+1)):
        if num%i ==0:
            c += 1
            break
        if c==1:
            print("it is not prime")
        else:
            print("its not prime no.")
else:
    print("enter another no.")    '''    

'''import sys 
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
 
i = 0
def add():
    global i 
    i +=1
    print("Hello",i)
    add() 
add()
'''

# def greet():
#     print("hello")
# greet()    

# def add(a,b):
#     return a+b
# a1 = add(100,200)
# print(a1)

# def add_sub(x,y):
#     c = x+y
#     d = x-y
#     return c,d
# result1,result2 = add_sub(40,60)
# print(result1,result2)

# def sum(a,*b):
#     c = a
#     for i in b:
#         c +=i
#         print(c)
# sum(10,20,30,40,)        

'''# def sum(a,*b):
#     c = 0
#     for i in b:
#         c=c+i
#         print(c)
# sum(10,20,30,40,50)    '''    
'''def fact(n):
    if n ==0:
        return 1
    return n*fact(n-1)
result = fact(5)
print(result)'''
'''def is_even(n):
    return n%2==0
nums = [11,12,23,24,55,77,66]
evens = list(filter(is_even,nums))
print(evens)

e1 = list(filter(lambda n:n%2==0,nums))
print(e1)
'''
'''nums = [1,2,3,4,5,11,22,33,44,55]
doubles = list(map(lambda n:n*2,nums))
print(doubles)

nums = [22,33,44,55,66]
doubles = list(map(lambda n:n*2,nums))
print(doubles)'''
'''
from functools import reduce
num = [1,2,34,5,5,6]
sum = reduce(lambda a,b:a+b,num)
print(sum)'''

'''def disp():
    def inner():
        print("inner function ")
    print("outer function")
    inner()    

disp()
'''
'''
def disp():
    def show():
        return "show function"
    result = show() 
    print("hello function")
    return result
print(disp())'''

# def disp(st):
#     def show():
#         return "show function"
#     result = show() + st +"disp function"
#     return result
# print(disp("hello world"))
'''def decor(func):
    def inner():
        print("before enhancement")
        func()
        print("after enhancement")
    return inner    


@decor
def add():
    print("hello")
    print("we will use this function")
add() '''

'''def decor(func):
    def inner():
        a = func()
        add = a+5
        return add
    return inner    

@decor
def num():
    return 10
num()
print(num())
'''
'''for i in range(1,20):
    if i%3==0 or i%5==0:
        continue
    print(i)

print("bye")      
'''

'''for i in range(1,101):
    if i%2==0 or i%5==0:
        pass
    else:
        print(i)
print("bye") '''      
'''def is_even(list1):
    even_num = []
    for i in list1:
        if i%2==0:
            even_num.append(i)
    return even_num
e1 = is_even([2,3,4,5,6,7,8,91,20])
print("even numbers in the given list are: ",e1)
'''
'''def is_even(list1):
    even_num = []
    for i in list1:
        if i%2==0:
            even_num.append(i)
    return even_num
e1 = is_even([12,22,223,443,333])
print("even numbers are: ",e1)      '''

'''for i in range(4):
    for j in range(4):
        print("#",end =" ")
    print()        
'''
'''for i in range(4):
    for j in range(i+1):
        print("#",end = " ")
    print()    '''

'''for i in range(4):
    for j in range(4-i):
        print("#",end = " ")
    print()    '''

'''s = input("Enter the value: ")
reverse = s[::-1]
print(reverse)'''

# num = 12345
# reversed_num = 0
# while num>0:
#     digit = num%10
#     reversed_num = reversed_num*10+digit
#     num = num//10
# print(reversed_num)   

# numbers = []
# for i in range(5):
#     item = float(input("enter the number: "))
#     numbers.append(item)
# print("User list",numbers)    

# str1,str2,str3 = input("enter three string with space : ").split()
# print("name1:",str1)
# print("name2:",str2)
# print("name3:",str3)


# str1,str2,str3 = input("enter three string with space : ")
# print("name1:",str1)
# print("name2:",str2)
# print("name3:",str3)

# from functools import reduce
# s = 0
# n = int(input("Enter the first number : "))
# range = range(n+1)
# sum = reduce(lambda s,n:s+n,range)
# print(sum)   
import csv 
f = open("data.csv","r")
row = csv.reader(f)
for i in row:
    print(i)