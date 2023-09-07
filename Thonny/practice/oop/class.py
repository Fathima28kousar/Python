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

e1 = Employee("rahul",123)
e2 = Employee("soniya",3444)

Employee.company_name = "Fortis"
print(Employee.company_name)

e2.company_name = "capegemini"
print(e2.company_name)
print(Employee.company_name)
'''