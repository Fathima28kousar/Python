# add = lambda x,y:x+y
# print(add(3,4))

# def my_func(n):
#     return lambda x: x*n
# add = my_func(2)
# print(add(5))
# from functools import reduce
# evens = [2,4,6,8]
# # x = (list(map(lambda n:n*2,evens )))
# # print(x)
# x = reduce(lambda x,y:x+y,evens)
# print(x)


# mylist = ["apple","mango","banana","peach"]
# sortedlist = sorted(mylist,key = lambda x:x[1])
# print(sortedlist)

# def my_func(n):
#     return lambda x: x + n

# adder = my_func(5)
# print(adder(10))

# def myfunc(n):
#     return lambda x: x + n
# result = myfunc(8)
# print(result(2))

# mylist = [1,2,3,45,6]
# newlist = [(lambda x:x+2)(x) for x in mylist]
# print(newlist)
# def decorator_lowercase(func):
#     def to_lower():
#         text = func()
#         lowercase_text = text.lower()
#         return lowercase_text

#     return to_lower  # returning inner function

# @decorator_lowercase
# def message():
#     return "I Am a Normal Function"

# print(message())

# def decor(func):
#     def lower_case():
#         text = func()
#         lowercase_text = text.lower()
#         return lowercase_text
#     return lower_case


# @decor 
# def message():
#     return "PYTHON IS AN EASY LANGUAGE"

# x = message()    
# print(x)

# for i in range(10):
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(1,10):
#     print(i,end="  ")        