# # def decor(fun):
# #     def inner():
# #         a = fun()
# #         add = a+5
# #         return add
# #     return inner
# # @decor
# # def num():
# #     return 10
# # result = num()
# # print(result)
# # def decor(fun):


# # @decor
# # def add():
# #     print("hello")
# # add()    
# def decor(func):
#     def inner(name):
#         if name == "modi":
#             print("pm")
#         else:
#             func(name) 
#     return inner

           

# @decor 
# def employee(name):
#     print("Hello,GM",name)
# employee("rahul")
# employee("sonia")    
# employee("priyanka")
# employee("modi")
# def smart_div(func):
#     def inner(a,b):
#         if b==0:
#            print("Division by zero is not allowed.")
#         else:
#             func(a,b)
#     return inner

# @smart_div
# def cal(a,b):
#     return a/b
# print(cal(10,2))
# print(cal(10,0))
# def verify(func):
#     def inner(name):
#         if name=="rahul":
#             print("not pm")
#         else:
#             func(name)
#     return inner            

# @verify
# def add(name):
#     print("hello",name)
# add("rahul")    
# def decor(fun):
#     def inner(*args,**kwargs):
#             print("before the function","before the function")
#             print("before the function","before the function")
#             fun(*args,**kwargs)
#             print("after the function")
#     return  inner     


# @decor 
# def greet(name,fame,lname):
#       print("Hello!",name,fame)

# greet("python","python","famr")
# def decor(fun):
#     def inner(*args,**kwargs):
#         print("before")
#         result = fun(*args,**kwargs)
#         print("after")
#         return result
#     return inner    
    


# @decor 
# def add(x, y ):
#     return x+y

# result = add(5,6)
# print(result)
# def decor_1(func):
#     def inner():
#         print("before")
#         func()
        
#     return inner

# def decor_2(func):
#     def inner():
#         print("b1")
#         func()
        
#     return inner        


# @decor_1
# @decor_2
# def greet():
#     print("hello")

# greet() 
# x = lambda n:n*2
# print(x(5))
# for i in [2,1,5]:
#     print(i)
    

   










