# def outer():
#     print("y")
#     a = 100
#     def inner():
#         print("g")
#         print(a)
#         outer()
#         inner()
# outer()
# def get_detail():
#     a = 100
#     print(a)
# get_detail() 
# a = 100
# def get_detail():
#     b = 200
#     print(a+b)
#     print(b)
#     print(a)
# get_detail()
# a = 100
# def get_detail():
#     global b
#     b=300
#     print(a + b)

# get_detail()
# print(a)
# print(b) 
# def outer(a,b):
#     return a + b
# outer(10,23)
  
# x = lambda a,b:a+b  
# print(x(10,20))

# def multiply(a,b,c):
#     return a*b*c
# print(multiply(10,20,30))

# rajni =lambda a,b,c: a*b*c
# print(rajni(10,20,30))
# def addone(mark):
#     return mark+1
# mark = [34,35,36,37,38]
# new_marks = map(addone,mark)
# type(new_marks)
# print(list(new_marks))
# enames = ["rahul","sonia","priyanka"]
# new_names = []
# for ename in enames:
#     new_names.append(ename.upper())
# print(enames) 
# print(new_names)
# enames = ["rahul","sonia","priyanka"]
# new = []
# for ename in enames:
#     new.append(ename.upper())
# print(enames) 
# print(new)   
# def add(a,b):
#     return a + b
# x = map(add,("apple","banana","cherry"),("hello"))
# print(x)
# print(list(x))

# lambda name : name.upper()
# data = map(lambda name :)
# def add(names):
#     return len(names)
# x = map(add,("sonia","rahul","priyanka"))
# print(x)
# print(list(x))
# def add(name):
#     return name.upper()

# x = map(add,("sonia","gandhi"))
# print(x)
# print(list(x))
# def add():
#     y = 20
#     return (lambda x:x+y)
# result = add()
# print(result(3))
# def show(a):
#     print(a(8))
# show(lambda x:x+5)   
# def add(n):
#     return lambda x:x*n
# result = add(7)
# print(result(3))
     