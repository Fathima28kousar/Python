# class Employee:
#     "hello world"
#     company_name = "TCS"
#     def __init__(self,sal,age):
#         self.sal = sal
#         self.age = age

#     def display(self):
#         print(self.sal,self.age)

#     def change_data(self):
#         self.age = 35
#         self.sal = 100
#     @classmethod
#     def get_company_name(cls):
#         cls.company_name = "Royal"
#         print(cls.company_name)
    
# e1 = Employee(1000,20)
# e2 = Employee(2000,40)
# Employee.get_company_name()


'''class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +"." +last+"@company.com"
    
    def fullname(self):
        return "{}{}".format(self.first,self.last)
    
e1 = Employee("atif ","aslam ",700)
e2 = Employee("fathima","kousar",1000)
'''

'''class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        Employee.num_of_emps+=1

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)  

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
        Employee.set_raise_amt(1.05)


e1 = Employee("tina","malhotra",200)
e2 = Employee("rahul","khanna",100)

e1.raise_amount = 1.05
print(e1.__dict__)
print(Employee.raise_amount)
print(e1.raise_amount)
print(Employee.num_of_emps)
print(Employee.__dict__)

'''

# class Employee:
#     bonus = 1.04
#     num_of_emps = 0

#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         Employee.num_of_emps+=1

#     def fullname(self):
#         return "{}{}".format(self.first,self.last)
    
#     def apply_raise(self):
#         self.pay = int(self.pay*self.bonus)


# e1 = Employee("fathima","kousar",40)
# e2 = Employee("Lubna ","sadiay",50)

# e1.bonus = 1.08
# print(e1.__dict__)
# print(Employee.bonus)
# print(Employee.apply_raise  )
# print(e1.bonus)
# print(e1.bonus)


'''class Employee:
    company_name = "TCS"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def design_name(cls):
        cls.design_name = "css"
        print(cls.design_name)
        print("THE DESIGN NAME IS-",cls.design_name)

e1 = Employee("rahul",123)
e2 = Employee("soniya",3444)

Employee.company_name = "Fortis"
print(Employee.company_name)

e2.company_name = "capegemini"
print(e2.company_name)
print(Employee.company_name)
Employee.design_name()'''

# class Bank:
#     bank_name = "BOI"
#     rate_of_interest = 12.25

#     @staticmethod
#     def simple_interest(prin,n):
#         si = (prin*n*Bank.rate_of_interest)/100
#         print(si)
# prin = float(input("Enter the principal amount:"))
# n = int(input("Enter the no. of years :"))
# Bank.simple_interest(prin,n)              
'''class Employee:
    bonus = 2000
    def display(self):
        print("Employee class method")

class Manager(Employee):
    bonus1 = 5000
    def show(self):
        print("Manager class method")

e1 = Employee()
m1 = Manager()

e1.display()
m1.display()
m1.show()

print(m1.bonus1)
print(e1.bonus)'''


''''class Computer(object):
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
        print("computer class constructor")

class Mobile(Computer):
    def __init__(self,ram,storage):
        self.model = 

a1 = Mobile()
print(a1.__dict__)'''

'''class Human_being(object):
    def __init__(self):
        print("human being constructor is called")
        self.name = input("Enter your name:")

class Employee(Human_being):
    def __init__(self):
        print("Employee constructor is called ")
        self.salary = float(input("Enter your salary:"))

class Manager(Employee):
    
    def __init__(self):
        print("Manager constructor is called")
        self.bonus = float(input("Enter the bonus: "))

m1 = Manager()
print(m1.salary)
print(m1.name)'''

# class Human_being(object):
#     salary = 1000
#     name1 = "Jayuuu"

# class Employee(Human_being):
#     salary = 2000
#     name = "Jay"

# class Manager(Employee):
#     salary = 5000

# m1 = Manager()

# print(m1.salary)
# print(m1.name1)
# print(m1.name)
# print(m1.__dict__)

# class Person:
#     def __init__(self,nm,ag):
#         self.name = nm
#         self.age = ag

#     def display0(self):
#         print("This is a person display method")
    
# class Employee(Person):
#     def __init__(self,nm,ag,sal):
#         super().__init__(nm,ag)
#         self.salary = sal

#     def display1(self):
#         print("This is a Employee display method")

# class Student(Person):
#     def __init__(self,nm,ag,m):
#         super().__init__(nm,ag)
#         self.marks = m

#     def display2(self):
#         print("This is a Student display method")

# s1 = Student("jay",21,90)  
# e1 = Employee("raj",45,30000)
# p1 = Person("fathima",24)
# print(e1)
# print(s1)
# print(e1.__dict__)
# print(s1.__dict__)
# print(p1.__dict__)

# s1.display0()
# e1.display0()
# # s1.display1()
# e1.display1()
# e1.display0()
# s1.display2()
 
# print(len("hello"))
# print(len(["h","el","lo"]))
# print(len({"key":"value","len":"value"}))


''''emp = ["jay","viru","ram"]
for i in reversed(emp) :
    print(i)

company ="infosys"
for i in reversed (company):
    print(i)'''

# class Veh:
#     def __init__(self,name,color,price):
#         self.name = name
#         self.color = color
#         self.price = price

#     def get_details(self):
#         print("name is ",self.name)
#         print("color is ",self.color)
#         print("price is ",self.price)

#     def max_speed(self):
#         print("maximum speed limit is 100kmph")

#     def gear(self):
#         print("gear change is 6")

# class Car(Veh):
#     def max_speed(self):
#         print("max speed limit is 140kmph")

#     def gear(self):
#         print("gear change is 9")

# v1 = Veh('truck',"red",2000)
# c1 = Car("car","white",700)
# # v1.get_details()
# # c1.get_details()

# v1.max_speed()
# v1.gear()
# c1.gear()
# c1.max_speed()

# class BMW:
#     def fuel_type(self):
#         print("diesel")

#     def max_speed(self):
#         print("max speed is 200")

# class Ferrari:
#     def fuel_type(self):
#         print("petrol")

#     def max_speed(self):
#         print("max speed is 180")

# def car_details(obj):
#     obj.fuel_type()
#     obj.max_speed()

# bmw = BMW()
# ferrari = Ferrari()
# car_details(bmw)

# print("-----------------")

# car_details(ferrari)
class Vehicle:
    color="white"
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
        

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

v1 = Vehicle("truck",30,"30kmph")
b1 = Bus("bus",29,"10kmph")
c1 = Car("car",45,"56kmph")
print(v1.color,v1.name,v1.max_speed)
print(v1.__dict__)
print("color:", v1.color, "name:", v1.name, "Speed:", v1.max_speed, "Mileage:", v1.mileage)

