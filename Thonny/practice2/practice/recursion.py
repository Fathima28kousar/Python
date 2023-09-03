# #recursion

# def greet():
#     print("hello")
#     print("yes")
#     greet()

# greet()

# import sys

# sys.setrecursionlimit(200)
# print(sys.getrecursionlimit())


# i = 0
# def greet():
#     global i 
#     i = i +1
#     print("Hello","yes",i)
#     print("yes",i)
#     greet()

# greet()

# def greet():
#     print("hello")
# greet()         
# def add(a,b):
#     c = a+b
#     print(c)
# add(4,5)
# def add(a,b):
#     c = a+b
#     return c  
# result = add(7,8)
# print(result)
# def add_sub(a,b):
#     c = a+b
#     d = a-b
#     return c,d
# result1,result2 = add_sub(10,20)
# print(result1,result2)
# def sum(a,*b):
#     c = a
#     for i in b:
#         c = c+i
#         print(c)
# sum(5,6,7,8,9)       

# def sum(*b):
#     c=0
#     for i in b:
#         c = c+i
#         print(c)
# def person(name, **data):
#     print(name)
#     print(data)
#     for i, j in data.items():
#         print(i, j)

# person("fathima", age=30030, city="bangalore")
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# result = fact(4)
# print(result)
# def is_odd(n):
#     return n%2 !=0

# def is_even(n):
#     return n%2==0

# nums = [1,34,54,67,88,7,5,433,55,44]
# evens = list(filter(is_even,nums))
# odds = list(filter(is_odd,nums))
# print(evens)
# print(odds)
# even = list(filter(lambda n: n%2==0,nums))
# print(even)
# evens = [34, 54, 88, 44]
# from functools import reduce
# doubles = list(map(lambda n:n*3,evens)) 
# print(doubles)

# sum = reduce(lambda a,b:a+b,doubles )
# print(sum)
# def disp():
#     def show():
#         print("show function")
#     print("disp function")
#     show()
# disp()
# def disp():
#     def show():
#         return "show function"
#     result = show() + "  disp function"
#     return result
# disp()
# print(disp())
# def disp (st):
#     def show():
#         return "show-function"
#     result = show()+st + " disp-functiion"
#     return result
# print(disp(" geeky-shows"))    
    
# def disp(st):
#     def show():
#         return "hello"
#     result = show() +st + " gm"
#     return result
# print(disp(" children"))
# def div(a,b):
#     if a<b:
#         a,b = b,a
#     print(a/b)
# div(2,4)    
# def decor(fun):
#     def inner():
#         print("If : Before enhancing")
#         fun()
#         print("If : After enhancing")
#     return inner
   

# @decor
# def num():
#     print("we will use this function")
#     print("we will enhance")
# num() 


