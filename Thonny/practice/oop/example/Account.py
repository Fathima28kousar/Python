from Bank import *

class Account(Bank):
    def __init__(self,id,name):
        print("Account class const")
        self.acc_id = id
        self.acc_name = name

    def cal_bal(self):
        pass
a = Account(101,"rahul")
print(id(a))