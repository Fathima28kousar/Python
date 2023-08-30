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

class Person:
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
        