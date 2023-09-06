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
class Account(Bank):
    def cal_bal(self):
        print("Bal is")
a1 = Account()
a1.cal_bal()