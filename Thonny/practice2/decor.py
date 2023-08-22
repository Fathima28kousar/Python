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
def decorator(func):
    def wrap(*args, **kwargs):
        # Log the function name and arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the return value
        print(f"{func.__name__} returned: {result}")
        
        # Return the result
        return result
    return wrap

# Example usage
@decorator
def multiply_numbers(x, y):
    return x * y

# Call the decorated function
result = multiply_numbers(10, 20)
print("Result:", result)










