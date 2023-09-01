# class Employee:
#     pass

# e1 = Employee()
# e2 = Employee()
# e3 = Employee()

# print(e1)
# print(id(e1))

# print(e2)
# print(id(e1))
# print(id(e2))

# class Myclass:
#     x = 4
# p1 = Myclass()   
# print(p1.x)    


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = Person("G",54)
# print(p1.name)
# print(p1.age)        

'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("G",40)
print(p1.name)                
print(p1.age) '''

# class Person:
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name
# p1 = Person("fathima",23)
# print(p1.name)
# print(p1)   
'''
class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def __str__(self):
        return f"{self.name},{self.age}"

p1 = Person("kousar",11)
print(p1)        '''


'''class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def myfunc(self):
        print("Hello this is "+self.name) 
p1 = Person("john",36)
p1.myfunc()    '''       

'''class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name) 

p1 = Person("john",12)
print(p1.age)  
p1.age = 45
p1.myfunc() 
print(p1.age)  
        '''




'''class Myclass:
    x = 5
print(Myclass)'''  

'''class Myobject:
    x = 10
p1 = Myobject()
print(p1.x) '''   

'''class Myclass:
    x = 200
p2 = Myclass()
print(p2.x)    '''

'''class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

p1 = Person("hero",12)
print(p1.age)
print(p1.name)
'''


'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p2 = Person("alexander",100)
print(p2.name)
print(p2.age)
'''
'''class Person:
    def __init__(self,age,name):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person(45,"rohan")
print(p1.age)
print(p1.name)
print(p1)'''

'''class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def myfunc(self):
        print("Hello i am ", self.name, ", My age is probably :", self.age)    

p1 = Person("john",29)
p1.myfunc()'''

'''class Person:
    def __init__(self,name,age):
        self.age = age 
        self.name = name

    


p2 = Person("john",44)
p2.age = 40
print(p2.age)
del p2.age 
print(p2.age)
del p2
print(p2)'''



'''class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"
     
        Employee.num_of_emps+=1

    def fullname(self):
        return "{}{}".format(self.first,self.last)   

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount) 


emp_1 = Employee("john","alexander",5400)
emp_2 = Employee("fathima","kousar",10000000)
emp_1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.apply_raise())
print(Employee.raise_amount)
print(emp_1.apply_raise())
print(emp_1.pay)'''

'''class Employee:
    raise_amount =1.04
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps +=1

    def fullname(self):
        return "{}{}".format(self.first,self.last)    
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

emp_1 = Employee("Rahul","Gandhi",5000)
emp_2 = Employee("Sonia","Gandhi",5000)
emp_2.raise_amount = 1.05
print(Employee.num_of_emps)
emp_2.apply_raise()
print(emp_1. __dict__)
print(emp_1.pay)
print(Employee.__dict__)
print(emp_2.pay)
'''
'''
class Computer:
    def config(self):
        print("i5,16 Gb,1tb")




com1 = Computer()
com2 = Computer()
Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()'''