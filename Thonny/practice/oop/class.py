class Employee:
    "hello world"
    company_name = "TCS"
    def __init__(self,sal,age):
        self.sal = sal
        self.age = age

    def display(self):
        print(self.sal,self.age)

    def change_data(self):
        self.age = 35
        self.sal = 100
    @classmethod
    def get_company_name(cls):
        cls.company_name = "Royal"
        print(cls.company_name)
    
e1 = Employee(1000,20)
e2 = Employee(2000,40)
Employee.get_company_name()








# print(Employee.company_name)
# print(e1.company_name)
# print(e2.company_name)
# Employee.company_name = "Infosys"
# print(Employee.company_name)
# e1.company_name = "Licious"
# print(e1.company_name)
# print(Employee.company_name)
# print(e1.__dict__)
# print(Employee.__dict__)
# # e1.change_data()
# e2.change_data()
# print(e2.__dict__)
# # e1.name = "Rahul"
# print(e1.__dict__)
# del e1.name
# print(e1.__dict__)
# print(e1.sal)
# e1.sal = 5000
# print(e1.sal)
# e2.display()
# print(Employee.__dict__)
# print(Employee.__doc__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(isinstance(e1,Employee))
