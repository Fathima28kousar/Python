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


class Computer(object):
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
        print("computer class constructor")

class Mobile(Computer):
    def __init__(self,ram,storage):
        self.model = 

a1 = Mobile()
print(a1.__dict__)