'''class Account:
    min_Bal = 500
    def __init__(self,id,name):
        print("constructor method")
        self.eid = id 
        self.name =  name

a1 = Account(111,"Rahul")
print(a1)
print(id(a1))
print(a1.__dict__)'''

'''class Account:
    def get_details(self):
        print(self)

    @classmethod
    def get_no_of_object(cls):
        print(id(cls))

a1 = Account()
print(a1)
print(id(a1))
print(a1.__dict__)

Account.get_no_of_object()

a1.get_details()'''

'''class Bank:
    min_Bal = 0
    @classmethod
    def set_Min_Bal(cls):
        cls.min_Bal = 600
Bank.set_Min_Bal()   
print(Bank.min_Bal)     
'''

'''class Account:
    count=0
    def __init__(self):
        Account.count +=1
    @classmethod    
    def object(cls):
        print(cls.count)

Account()        
Account()        
Account()        
Account()        
Account() 
print(Account.count)
Account.object()       '''


# class Test:
#     '''created by Emp:Narasimha'''
#     pass

# print(Test.__dict__)
# print(Test.__doc__)


'''class Utility:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b
    
    @staticmethod
    def mult(a,b):
        return a*b
    
    @staticmethod
    def divi(a,b):
        return a//b
    
obj = Utility()  
print(obj.add(10,20))'''

# class Person:
#     '''Running from person class'''
#     @classmethod
#     def show_details():
#         print("Running from person class")

# p1 = Person()
# print(p1.show_details)        
# print(p1.__doc__)

# class Person:
#     @classmethod
#     def show_details(cls):
#         print(f"Running from {cls.__name__} class.")

# a1 = Person()
# print(a1.show_details()) 

'''class Person:
    @classmethod
    def show_details(cls):
        print(f"Running from {cls.__name__} class.")
    
Person.show_details()    
'''

'''class Container:
    @classmethod
    def show_details(cls):
        print(f"running from {cls.__name__} class.")
        print(cls.__dict__)

c1 = Container()
c1.show_details()
'''
class Person:
    lists = []
    count = 0

    def __init__(self):
        Person.lists.append(self)

    @classmethod
    def count_lists(cls):
        return len(Person.lists)
p1 = Person()
p2 = Person()
print(Person.count_lists())