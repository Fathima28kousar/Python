# apple = '''hello
# world 
#              i want to eat an apple        
#       hey how are you  
             
#                     coding        '''
# # for ch in apple:
# # #     print(ch)
# # nm = "harry"
# # print(nm[-4:-2])   
# nm = "!!!Harry!!!!  !!!!Harry!!!  !Harry!!!!!  !Harry!!!!!!!!  !!!"
# print(nm) 
# print(nm.lower())
# print(nm.upper())
# print(nm.rstrip("!"))
# print(nm.lstrip("!"))
# print(nm.replace("Harry","john"))
# print(nm.split(" "))

# aim = "introduction tO pythoN"
# print(aim.capitalize())
# print(aim.title())

# str1 = "Welcometos9console"
# # print(len(str1))
# # print(len(str1.center(50)))
# # print(str1.endswith("to",4,10))
# # print(str1.find("is"))
# # # print(str1.index("w"))
# print(str1.isalnum())
# print(str1.isalpha())
# str1 = "we wish you  a merry\n christmas"
# print(str1)
# print(str1.isprintable())


# str2 = "hello world"
# print(str2.isspace())
# str1 = "To kill a mocking bird"
# print(str1.istitle())
# str1 = "World Health "
# print(str1.istitle())
# print("max"[::-1].startswith("x"))
# print(max("my name is"))
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


def decor(func):
       def inner():
              print("something before")
              func()
              print("something after")
       return inner   



@decor 
def say_hello():
    print("Hello")

say_hello()    


# ef decor(func):
#     def inner():
#         print("something before")
#         func()
#         print("something after")
#     return inner

# @decor 
# def say_hello():
#     print("Hello")

# say_hello() 
