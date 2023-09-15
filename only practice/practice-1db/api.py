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


    
    
            

 