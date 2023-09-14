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

'''import time
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
        
withdraw()'''
'''
import random
name = input("What is your name? ")
print("Good luck ",name)
word_list = ["apple","watermelon","orange","pear","cherry","atrawberry","nectarine","grape"]
word = random.choice(word_list)

print("Guess the character ")
guesses = " "

turns =4
while turns>0:
    failed =0

    for char in word:
        if char in guesses:
            print(char,end =" ")
        else:
            print("_",end=" ")
            failed+=1

    if failed ==0:
        print("\n You win !!! YAY !!!")
        print("The word is ",word)
        break
    print()

    guess = input("Guess a character : ")
    guesses +=guess
    guess = guess.lower()

    if guess not in word:
        turns-=1
        print("Wrong")
        print("You have ",turns," more guesses")

        if turns ==0:
            print("You lose!!!")
            print("the correct word is ", word)

    print("Your guessed characters are ",guesses)'''

'''import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response)
print(type(response))

todo_data = response.json()
print(todo_data)

# Iterate through the JSON data and print the keys and values
for key, value in todo_data.items():
    print(f"{key}: {value}")
'''

# import requests
# import json

# response = requests.get("https://jsonplaceholder.typicode.com/users")
# data = response.json()
# print(data)
# print(type(data))
# for user in data:
#     print(user["id"],":",user["name"])

# fp = open("emp.json","w")
# json.dump(data,fp)
# fp.close
import mysql.connector

# Replace these placeholders with your database credentials
host = "your_host"
user = "your_user"
password = "your_password"
database = "your_database"

# Create a connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to interact with the database
cursor = connection.cursor()


