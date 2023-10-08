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
# import pymongo
# if __name__=="__main__":
#     print("Welcome to mongo db")
#     client = pymongo.MongoClient("mongodb://localhost:27017")
#     print(client)
#     db = client['kousar']
#     collection = db['dbsample']
    # dictionary = {'name':'fathima','marks':34,'location':'new york','age':59}
    # collection.insert_one(dictionary)
    # insertThese = 
    # collection.insert_many(insertThese)
    # one = collection.find_one({'name':'fathima'})
    # print(one)
    # all = collection.find({'gender':'Male'})
    # for item in all:
    #     print(item)
    # all = collection.find({'name':'fathima'},{'name':0})
    # for item in all:
    #     print(item)
    # count = collection.count_documents({'name':'fathima'})
    # print(count)
    # allDatabases = client.list_database_names()
    # print(allDatabases)
    # col = client['kousar']
    # print(col.list_collection_names())
    # prev = {'name':'fathima'}
    # nextt = {'$set':{'location':'America'}}
    # up =collection.update_many(prev,nextt)
    # print(up.modified_count)
    # rec = {'name':'fathima'}
    # up =collection.delete_one(rec)
    # print(up.deleted_count)
    # rec = {'name':'fathima'}
    # up =collection.delete_many(rec)
    # print(up.deleted_count)
    # all = collection.find({'name':'fathima'})
    # print(collection.count_documents({'name':'fathima','marks':{"$lte":100}}))
    # print(collection.count_documents({}))
'''import csv
f = open('data.csv','r')
d = csv.reader(f)
next(d)
max =0
for i in d:
    if int(i[4])>max:
        max = int(i[4])
f.close()
f = open('data.csv','r')
d =csv.reader(f)
next(d)
for i in d:
    if int(i[4]) ==max:
        print("Roll_number: ",i[0])
        print("Name: ",i[1])
        print("Class: ",i[2])
        print("Section: ",i[3])
        print("Marks: ",i[4])
f.close()'''

'''import csv
import os
f = open('data.csv','r')
d = csv.reader(f)
f1 = open('data0.csv','w',newline='')
d1 = csv.writer(f1)
next(d)
roll_no = int(input("Enter the roll number: "))
mn = input("Enter the modified name: ")
mc = input("Enter the modified class: ")
ms = input("Enter the modified section: ")
mm = int(input("Enter the modified marks: "))
mr = [roll_no,mn,mc,ms,mm]
header = ['Roll_no.','Name','Class','Section','Marks']
for i in d:
    if int(i[0]) ==roll_no:
        d1.writerow(mr)
    else:
        d1.writerow(i)
f.close()
f1.close()

os.remove('data.csv')
os.rename('data0.csv','data.csv')'''
'''
import csv
f = open('data.csv','r')
d = csv.reader(f)
next(d)
count =0
for i in d:
    count+=1
print(count)
'''
# import csv 
# f = open('data.csv','r')
# d = csv.reader(f)
# next(d)
# s = 0
# for i in d:
#     if len(i)>=5:
#         s += int(i[4])
# print("total marks are: ",s)
# f.close()
'''import csv
f = open('data.csv','r')
d = csv.reader(f)
next(d)
found = False
for row in d:
    if len(row)>=5 and int(row[4])>90:
        print("Roll number is: ",int(row[0]))
        print("Name: ",(row[1]))
        print("Class: ",(row[2]))
        print("Section: ",(row[3]))
        print("Marks: ",(row[4]))
        found = True
if not found:
    print("Record not found")
f.close()'''
'''import csv
f = open('data.csv','r')
f1 = open('data0.csv','w',newline='')
d = csv.reader(f)
d1 = csv.writer(f1)
for i in d:
    d1.writerow(i)
f.close()
f1.close()'''
'''import csv
field = ['roll_number','name','class','section','marks']
f = open('data0.csv','w',newline='')
d = csv.writer(f)
d.writerow(field)
ch = 'y'
while ch=='y' or ch=='Y':
    rn = int(input("Enter the roll number: "))
    nm = input("Enter the name: ")
    ma = int(input("Enter the marks: "))
    mr = [rn,nm,ma]
    d.writerow(mr)
    ch = input("Enter more record (Y/N): ")
f.close()'''
'''import csv 
f = open('data.csv','r')
d = csv.reader(f)
next(d)
roll = int(input("Enter the roll number: "))
found = False
for i in d:
    if len(i)>=5 and int(i[0]) == roll:
        print("Roll number: ",i[0])
        print("Name: ",i[1])
        print("Class: ",i[2])
        print("Section: ",i[3])
        print("Marks: ",i[4])
        found = True
if not found:
    print("Record not found")
f.close()'''
# import csv 
# f = open('data0.csv','r')
# row = csv.DictReader(f)
# for i in row:
#     print(i)
'''import csv
f = open('data0.csv','r')
row = csv.DictReader(f,fieldnames=['roll','name','class'])
for i in row:
    print(i)'''
'''import csv
f = open('data.csv','r')
d = csv.reader(f)
next(d)
next(d)
next(d)
for row in d:
    if len(row)>=5:
        print(row[0],row[2])
'''
# a,b,c = input("Enter values: ").split()
# print("First no. is {} second number is {} and third name is {}".format(a,b,c))

# x = list(map(int,input("Enter values: ")))
# print("list of students: ",x)

# num = int(input("Enter the number: "))
# letters = ['','one','two','three','four','five','six','seven','eight','nine']
# def word_of_number(num):
#     if num ==0:
#         return 'zero'
#     elif num>0:
#         return letters[num]
# w = word_of_number(num)
# print("The word of the number is: ",w)

# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))
# num3 = int(input("Enter the number: "))
# greatest =max(num1,num2,num3)
# print("The greatest number among three is ",greatest)

# number = int(input("Enter the number: "))
# for i in range(1,11):
#     result = number*i
#     print(result)

# print()

# number = int(input("Enter number: "))
# i = 0
# while i<10:
#     i+=1
#     result = number*i
#     print(result)


