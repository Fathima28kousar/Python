'''class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
        Employee.num_of_emps+=1
    
    def apply_raise(self):
        return int(self.pay*self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
        Employee.set_raise_amt(1.05)

    @classmethod
    def from_string(cls,emp_str):
        first


emp1 = Employee("john",1000)'''
class Person:
    def __init__(self,name,ag):
       self.name = name
       self.age = ag

class Employee(Person):
    def __init__(self,sal):
        self.salary = sal

class Student(Person):
    def __init__(self,marks):
        self.marks = marks
s1 = Student("john",12)
e1 = Employee("raj",45)

