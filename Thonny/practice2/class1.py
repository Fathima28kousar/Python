'''class Test:
    a = 100
    def __init__(self):
       Test.b = 200

    def m1(self):
        Test.c = 300

    @classmethod
    def m2(cls):
        cls.d = 400
        Test.e = 500

    @staticmethod
    def m3():
        Test.f = 449  '''        

'''class Employee:
    org_name = "TCS"

    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    @classmethod
    def cal_Age(cls):
        pass

    def get_details(self):
        pass    


e1 = Employee(101,"Rahul",12)
print(e1)     '''

'''class Employee:
    org_Name = "Tcs"
    @classmethod
    def call_Age(cls):
        print(cls.__dict__)

    def get_Details(self):
        print(self.org_Name)
        print(Employee.org_Name)
'''
###
'''class Account:
    def __init__(self,id,name,amount):
        self.acc_id = id
        self.acc_name = name
        self.acc_amount = amount

    def set_Email(self,email):
        self.acc_email = email  

a1 = Account(101,"rahul",45000)    
a2 = Account(102,"gandhi",2000)  
print(a1.__dict__)
print(a2.__dict__)  
a1.set_Email("rahul@gmail.com")
a2.set_Email("gandhi@gmail.com")
print(a1.__dict__)
print(a2.__dict__)

a1.loc = "waynad"
print(a1.__dict__)
print(a2.__dict__)
'''

'''class Account:

    def __init__(self,id,name):
        self.id = id
        self.name = name
        Account.branch_Code = 5657

a1 = Account(101,"rahul")
a2 = Account(102,"sonia")

print(a1.__dict__)
print(a2.__dict__)

print(Account.__dict__)'''
'''
class Employee:
    org_Name = "TCS"

    @classmethod
    def cal_Age(cls):
        print(cls.__dict__)

    def get_Details(self):
#        print(cls.org_Name)    
        print(self.org_Name)
        print(Employee.org_Name)

e1 = Employee()
e2 = Employee()

Employee.cal_Age()

print(e1.__dict__)
print(e2.__dict__)
print(Employee.org_Name)
print(Employee.__dict__)'''



