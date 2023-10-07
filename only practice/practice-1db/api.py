'''import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/comments?10")
users_lists = response.json()
print(type(users_lists))
print(users_lists)
for user in users_lists:
    print(user["id"],user["email"])

    fp = open("user.json","w")
    json.dump(users_lists,fp)
fp.close()'''

# import
#  mysql.connector
# connection = mysql.connector.connect(host="localhost",user="root",password="FKW#84#kousar",database="fathima" )
# cursor = connection.cursor()

# create_table_query = """
# CREATE TABLE IF NOT EXISTS table1(
# id INT PRIMARY KEY,
# name VARCHAR(255),
# age INT
# )
# """
# cursor.execute(create_table_query)

# insert_data_query ="""
# INSERT INTO table1(id,name,age)
# VALUES(%s,%s,%s)
# """

# data_to_insert =[
#     (101,"john",30),
#     (102,"bear",32),
#     (103,"grils",33),
#     (104,"gordan",20),
# ]

# cursor.executemany(insert_data_query,data_to_insert)

# connection.commit()
# cursor.close()
# connection.close()

'''import requests
import csv

response = requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code ==200:
    data = response.json()
    fp = open("data.csv","w", newline='')
    csv_writer = csv.writer(fp)
    if len(data)>0:
        header = data[0].keys()
        csv_writer.writerow(header)

        for item in data:
            csv_writer.writerow(item.values())
    fp.close()
    print("API has been written",data)
else:
    print("Api request failed",response.status_code)'''


'''
API URL: https://dummyjson.com/products/1
Method Type:GET
AccessType:Public 
Requied filed: None
'''
# #invokie Rest api and print user names
# import requests 
# import json 

# response=requests.get('https://jsonplaceholder.typicode.com/users')

# users=response.json()
# print(type(users))
# print(users)

# for user in users:
#     #print(type(user))
#     print(user['name'])

#invoke rest api and write into new json file
#invoke rest api and write into new json file
# '''import random 

# name = input("What is your name? ")
# print("Good Luck ",name,"!")

# words = ["apple","hello","hi"]
# word = random.choice(words)

# guesses = " "

# turns=10
# while turns>0:
#     failed=0

#     for char in word:
#         if char in guesses:
#             print(char,end="")

#         else:
#             print("_",end=" ")
#             failed+=1
        
#     if failed ==0:
#         print("\n\'you win\' ")
#         print("The word is ",word)
#         break

#     print()

#     guess = input("Enter the character: ")
#     guesses +=guess
#     guess = guess.lower()

#     if guess not in word:
#         turns-=1
#         print("Wrong")
#         print("You have ",turns,"more turns")

#         if turns ==0:
#             print("You loose!")
#             print("The correct word is: ",word)'''

# '''import re
# data = '''abb Bengaluru airoepb_zebra fizzy  685904 049airoepb'''
# pattern = r'\d'
# match = re.findall(pattern,data)
# print(match)

'''import re
ip = '123.04483.0584.033.033.05.06.0'
string = re.sub('\.[0]*','.',ip)
print(string)'''
'''import re 
data = '56489 5789'
pattern = r'^5*'
match = re.findall(pattern,data)
print(match)
'''
import re 
pattern = r'dog|cat'
data = 'dog Dog cat Cat'
match = re.findall(pattern,data,re.IGNORECASE)
print(match)