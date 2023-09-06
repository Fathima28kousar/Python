# class Bank:
#     pass
# print(Bank)
'''
class Bank:
    def __init__(self):
        pass
    def get_accId(self):
        pass
    @classmethod
    def get_min_bal(cls):
        pass
    @staticmethod
    def cal_interest():
        pass

print(Bank)    '''
from abc import *
class Bank(ABC):
    
    @abstractmethod
    def cal_bal(self):
        pass
    
class Account(Bank):
    def cal_bal(self):
        print("Bal is low")
    

a1=Account()
a1.cal_bal()

from abc import *
class Bank(ABC):
    @abstractmethod
    def cal_bal(self):
        pass
# class Account(Bank):
#     def cal_bal(self):
#         print("Bal is")
# a1 = Account()
# a1.cal_bal()

from abc import ABC,abstractmethod

class Car (ABC):
    @abstractmethod
    def mileage(self):
        pass
    def color(self):
        print("white")

class Maruti_suzuki(Car):
    def mileage(self):
        print("mileage is 30 kmph")

 
class TATA(Car):
    def mileage(self):
        print("mileage is 35 kmph")    


class Duster(Car):
    def mileage(self):
        print("mileage is 40 kmph")           

m1 = Maruti_suzuki()
t1 = TATA()
d1 = Duster()
t1.mileage()