# # def add():
# #     print("addition")
# # add()    
# # def add(a,b):
# #     print(a+b)

# # add(10,20)    
# # add(1,2)
# # add(90,80)    
# # def add():
# #     print()    #type error as positional and actual arguments are not same
# # add(10,20)    

# # def cal_age():
# #     return 40

# # age = cal_age()
# # print(age)   
# # def add(a,*b):
# #     print(a,b)
# # add(10,20)    
# # add(10,20,30)    
# # add(10,20,30,40)    
# # add(10,20,30,40,50)    

# # def add(a,*b):
# #     pass
# # add(10,20)    
# # add(10,20,30)    
# # add(10,20,30,40)    
# # add(10,20,30,40,50)  
# # def cal_age(year):
# #     c_year = 2023
# #     return c_year-year
# # x1= cal_age(1983)
# # x2 = cal_age(1993)
# # x3 = cal_age(2003)
# # print(x1)
# # print(x2)
# # print(x3)
# # def calc(a,b):
# #     return a+b
# # x = calc(20,10)
# # y = calc(10,20)
# # print(x)
# # print(y)

# # def calc(a,b):
# #     return a-b
# # x = calc(10,20)
# # y = calc(20,10)
# # print(x)
# # print(y)
# # def cal():
# #     return 10,20,30
# # r1 = cal()
# # print(r1)
# # def calc():
# #     return 10,20,30,40
# # r1 = calc()
# # for value in r1:
# #     print(value)
# # def calc(a,b,c):
# #     pass
# # calc(10,20)
# # calc(10,20,30)

# # def calc(a,b,c=1):
# #     return a+b+c

# # r1 = calc(10,20)
# # r2 = calc(10,20,30)
# # print(r1)
# # print(r2)
# def wish(id,ename):
#     print("EmpId:", id,"EmpName:", ename)

# wish(id=101, ename="Rahul")    
# wish(ename ="Rahul", id = 101)

# # def wish(eid,ename):
# #     print("Employee Id:", eid, "- Employee Name:", ename)

# # wish(101,'Rahul')
# # wish('Rahul',101)
# def wish(eid,ename):
#     print("empid:",eid,"empname:",ename)

# wish(101,"rahul")
# wish("rahul",101)   

# def my_function():
#     print("Hello from a function") 

# my_function()   
# def my_function(fname):
#     print(fname + " hw are you?")
# my_function("hey")    
# my_function("hello")    
# my_function("hi")    

# def my_function(fname,lname):
#     print(fname+ " " + lname)
# my_function("fathima","kousar")    
# my_function("fathima","kousar")    
# my_function("fathima","kousar")    
# my_function("fathima","kousar")    

# def my_function(*kids):
#     print("The youngest child is " + kids[0])
# my_function("fathima","kousar","lubna","sadiya")    
# def my_function(child1,child2,child3):
#     print("The youngest child is " + child3)

# my_function("fathima","kousar","lubna")    
# def my_function(**kid):
#     print("her last name is " + kid["lname"])

# my_function(fname="fathima",miname="lubna",lname ="kousar")
# def my_function(city = "Bengaluru"):
#     print("i am from " + city)
# my_function("sweden")    
# my_function()    
# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ["apple ","mango","banana"]
# my_function(fruits)        
# def my_function(x):
#     return 5*x
# print(my_function(3))
# print(my_function(4))
# print(my_function(5))
def calc(a,b,c=0):
   return a+b+c
r1 = calc(10,20)
r2 = calc(10,20,30)
print(r1)
print(r2)
