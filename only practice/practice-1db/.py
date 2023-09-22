# import mysql.connector
# db = mysql.connector.connect(host="localhost",user ="root",password ="FKW#84#kousar",database="health")
# dbcursor = db.cursor()

# sql_insert = """
#     insert into Hospital values("5","shama clinic",200)
# """

# dbcursor.execute(sql_insert)
# db.commit()
# dbcursor.close()
# db.close()

'''import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="FKW#84#kousar",database="health")
dbcursor = db.cursor()

sql_insert = """
    insert into Hospital values(%s,%s,%s)
"""

data = [
    ("7","sankara hospital",300),
    ("8","manipal hospital",100)
]

dbcursor.executemany(sql_insert,data)
db.commit()
dbcursor.close()
db.close()
'''
# import mysql.connector
# db = mysql.connector.connect(host="localhost",user ="root",password="roots",database="company1")
# dbcursor = db.cursor()

# sql_create ="""
#     CREATE TABLE employee1(
#     eid INT NOT NULL,
#     name VARCHAR(50),
#     salary INT DEFAULT 20000,
#     location VARCHAR(50)
#     )
# """
# dbcursor.execute(sql_create)
# db.commit()
# dbcursor.close()
# db.close()
'''import mysql.connector
db = mysql.connector.connect(host="localhost",user ="root",password="roots",database="company1")
dbcursor = db.cursor()

sql_st="""
    insert into employee1 values(%s,%s,%s,%s)
"""
data = [
    (102,"rahul",6500,"delhi"),
    (103,"priyanka",7500,"mumbai"),
    (104,"modi",4000,"gujarat")
]

dbcursor.executemany(sql_st,data)
db.commit()
dbcursor.close()
db.close()
'''
# import mysql.connector
# try:
#     conn = mysql.connector.connect(
#         host= "localhost",
#         user="root",
#         password = "roots",
#         database="codeyug1"
#     )

#     if conn.is_connected():
#         print("Connected!")

# except Exception as obj:
#     print("Not connected")

# cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS tutorial1(
#             id INT PRIMARY KEY,
#             name VARCHAR(50),
#             views INT,
#             watchtime FLOAT
#             )""")
# cur.execute("DESC tutorial1")
# for data in cur:
#     print(data[0])    
# sql = """
#     INSERT INTO tutorial1(id,name,views,watchtime)VALUES(101,"OOP basics",1500,10)
# """
# cur.execute(sql)

# conn.commit()

# cur.close()
# conn.close()
# import time

# while True:
#     # Get the current time
#     current_time = time.strftime('%H:%M:%S %p')
    
#     # Print the current time to the console
#     print(current_time, end='\r',flush=True)
    
#     # Wait for 1 second before updating the time again
#     time.sleep(1)


# import random

# def number_guessing_game():
#     # Generate a random number between 1 and 100
#     secret_number = random.randint(1, 100)
    
#     # Initialize variables
#     attempts = 0
#     max_attempts = 10
    
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
    
#     while attempts < max_attempts:
#         try:
#             guess = int(input("Guess the number: "))
            
#             if guess < 1 or guess > 100:
#                 print("Please enter a number between 1 and 100.")
#                 continue
            
#             attempts += 1
            
#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
#                 break
        
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
    
#     if attempts == max_attempts:
#         print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

# if __name__ == "__main__":
#     number_guessing_game()


# num1 = 10
# num2 = 20
# print(num1+num2)
# print(num1.__add__(num2))
# print(int.__add__(num1,num2))
# print(dir(int))

# num = int(input("Enter any numbet between 1500 and 2700: "))
# for i in range(1500,2701):
#     if num%7==0 or num%5==0:
#         print("it is divisible by both")

#     else:
#         print("divisible")



# class Finance:
#     def __init__(self):
#         self.revenue = 10000
#         self.number_of_sales = 114

# f1 = Finance()
# print(f1.__dict__)

# class HR:
#     def __init__(self):
#         self.number_of_emp =32
#         f1.revenue = 1
        
# h1 = HR()
# print(h1.__dict__)
# print(f1.__dict__)

class Finance:
    def __init__(self):
        self.__revenue = 1000
        self.__number_of_sales=114

f1 = Finance()
print(f1.__dict__)
print(f1.revenue)
print(f1.number_of_sales)