'''class FiveDivisionError(Exception):
    pass

try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter second number: "))
    if n2 ==5:
        raise FiveDivisionError
    div = n1/n2
    print("division is :",div)

except (FiveDivisionError,ZeroDivisionError) as var:
    print(var)
print("Rest of the code")'''

import time
class BalanceExceptionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass
attempts = 1
def withdraw():
    global attempts
    saved_pin = 1234
    balance = 10000
    pin = int(input("Enter the pin: "))
    if pin == saved_pin:
        try:
            amt = float(input("Enter the amount: "))
            temp_bal = balance-amt
            if temp_bal<1000:
                raise BalanceExceptionError("Insufficient balance")
            balance = balance-amt
            print("Remained balance is",balance)
        except Exception as var:
            print(var)
    else:
        ans = input("Do you want to continue (Y/N):")
        if ans.lower() =="y":
            attempts +=1
            try:
                if attempts ==4:
                    raise AttemptExceptionError("Too many Attempts,Your account is blocked for an hour")
            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withdraw()
        else:
            print("Thank You!!!")
            return
        
withdraw()





