# #Write a Python program to find out what version of Python you are using.
# '''import sys
# print(sys.version)
# print(sys.version_info)'''

# # Write a Python program to display the current date and time.
# #Sample Output :
# #Current date and time :
# #2014-07-05 14:34:14

# '''import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))
# '''
# #Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# '''import math
# r = float(input("Enter the radius: "))
# print("Area is : ",(math.pi)*(r**2) )'''

# # Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# '''first = input("Enter the first name: ")
# last = input("Enter the last name: ")
# print(first[::-1]," ",last[::-1])
# print(last ," ",first)'''

# #Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# #Sample data : 3, 5, 7, 23
# #Output :
# #List : ['3', ' 5', ' 7', ' 23']
# #Tuple : ('3', ' 5', ' 7', ' 23')

# '''list=[ ]
# tuple=( )
# for i in range(5):
#     letter = input("Enter a letter: ")
#     list.append(letter)
#     tuple += (letter,)

# print(list)
# print(tuple)'''


# '''values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)
# '''
# #Write a Python program that accepts a filename from the user and prints the extension of the file.
# '''filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))'''
# #Write a Python program to display the first and last colors from the following list.
# '''color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])'''

# #Write a Python program that prints the calendar for a given month and year.
# '''import calendar 
# y = int(input("Enter the year: "))
# m = int(input("Enter the month"))
# print(calendar.month(y,m))
# '''
# #Write a Python program to print the following 'here document'.

# '''print("""
# a string that you "don't" have to escape 
# This 
# is a  ....... multi-line
# heredoc string -------> example
# """)'''

# #Write a Python program to calculate the number of days between two dates.
# '''from datetime import date
# fdate = date(2017,7,2)
# ldate = date(2017,7,11)
# data = ldate-fdate
# print(data.days)
# '''
# #convert string to float integer
# '''n = "344.5889435974530739059"
# print(int(float(n)))
# '''
# #Write a Python program that displays your name, age, and address on three different lines
# '''def personal_details():
#     name ="fathima"
#     age = 19
#     address = "bangalore"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name,age,address))

# personal_details()'''

# # Write a Python program to add two objects if both objects are integers.
# '''def add_objects(obj1,obj2):
#     if isinstance(obj1,int) and isinstance(obj2,int):
#         return obj1+obj2
    
#     else:
#         return "Both are not integers"
    
# object1 = 5
# object2 = 10

# result = add_objects(object1,object2)
# print("Result is: ",result)'''

# #Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
# '''def add(a,b):
#     if a==b or a+b==5 or a-b ==5:
#         return True
#     else:
#         return False
    
# a1 = add(10,5)
# print(a1)
# a2 = add(5,5)
# print(a2)
# print(add(7,2))
# '''
# # Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
# '''def add(a,b,c):
#     if a==b or b==c or c==a:
#         return a+b+c ==0
    
#     else:
#         return a+b+c
# print(add(10,2,1))
# '''
# #
# '''color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print(color_list_2.difference(color_list_1))
# print(color_list_1.difference(color_list_2))'''



# # youtuber = "Kylie Ying" # some string variable
# # print("subscribe to " + youtuber)
# # print("subscribe to {}".format(youtuber))
# # print(f"subscribe to {youtuber}")



# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed!")
    else:
        print(f"Task '{task}' not found!")

# Function to display the current tasks
def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Display tasks")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


