# class Account:
    
#     #instance method
#     def cal_bal(self):
#         print("cal_bal method -0 arg")
#     def cal_bal(self,a):
#         print("cal_bal method -1 arg")

#     def cal_bal(self,a,b):
#         print("cal_bal method -2 arg")


# a1= Account()
# a1.cal_bal()

#''''1
''''from Bank import * 

class Account(Bank):
    
    def __init__(self):
        pass
    def open_account(self):
        print('account opened successfully')
    def deposit_amount(self):
        pass
    
    def cal_bal(self):
        print('account class - cal_Bal')


Account()'''

#2
'''from Bank import * 

class Account(Bank):
    
    def __init__(self,aid,name):
        self.acc_id  = aid 
        self.acc_name = name
    #setter and getter - instance method

    def open_account(self):
        print('account opened successfully')
    
    def deposit_amount(self):
        pass

    def cal_bal(self):
        print('account class - cal_Bal')


#Account()'''

#3
'''
from abc import *
class Bank(ABC):
    @abstractmethod
    def cal_bal(self):
        pass'''

#4
'''from Account import * 

class  CA(Account):
    
    #static variable 
    min_bal = 5000
    def __init__(self,aid,name,amount):
        super().__init__(aid,name)
        self.acc_amount = amount
    def get_min_Bal(self):
        return self.min_bal 
    
    def deposit_amount(self,amount):
        self.acc_amount = self.acc_amount + amount 
    
    def cal_bal(self):
        return self.acc_amount - self.min_bal 



#a2=CA(102,'sonia',70001)
#a2.deposit_amount(60)
#print(a2.cal_bal())'''

#5
'''from Account import * 

class SA(Account):
    #static variable
    min_bal  = 500
    def __init__(self,aid,name,amount):
        super().__init__(aid,name)
        self.acc_amount = amount

    def get_min_Bal(self):
        return self.min_bal

    def deposit_amount(self,amount):
        self.acc_amount = self.acc_amount + amount 

    def cal_bal(self):
        return self.acc_amount - self.min_bal

#a1=SA(101,'rahul',50001)
#a1.deposit_amount(10)
#print(a1.__dict__)
#print(a1.cal_bal())'''

#6
'''from Account import *

from SA import * 
from CA import * 

def generate_AccountBal(obj):
    print(obj.cal_bal())

accounts=[SA(103,'Abhilash',80000),CA(104,'Vamsi',90000)]

for account in accounts:
    generate_AccountBal(account)'''