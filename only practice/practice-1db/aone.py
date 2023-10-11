# import mysql.connector

# connection = mysql.connector.connect(host="localhost", user="root", password="FKW#84#kousar", database="health")
# cursor = connection.cursor()

# # Check if the table 'vice' already exists
# cursor.execute("SHOW TABLES LIKE 'vice'")
# table_exists = cursor.fetchone()

# if not table_exists:
#     create_table = """
#         CREATE TABLE vice(
#             Hospital_Id INT UNSIGNED NOT NULL,
#             name VARCHAR(32),
#             bed_count INT,
#             PRIMARY KEY(Hospital_Id)
#         )
#     """
#     cursor.execute(create_table)

# # Rest of your code for inserting data

# cursor.close()
# connection.close()
'''num = 24
reverse_num = 0

while num > 0:
    remainder = num % 10
    reverse_num = reverse_num * 10 + remainder
    num = num // 10

print(reverse_num)'''

'''
num = int(input("Enter the number: "))
num_str =str(num)
reverse_num =' '
for i in reversed(num_str):
    reverse_num+=i
reverse_num = int(reverse_num)
print(reverse_num)'''

'''L = []
while True:
    line = input("Enter a sequence(or 'q' to quit): ")
    if line.lower() == 'q':
        break
    L.append(line.lower())
print("Sentences are: ")
for sentence in L:
    print(sentence)'''
'''import re 
data = input("Enter the password: ")
x = True
while x:
    if (len(data)<6 or len(data)>12):
        break
    elif not re.search("[a-z]",data):
        break
    elif not re.search("[A-Z]",data):
        break
    elif not re.search("[0-9]",data):
        break
    elif not re.search("[$%&#@]",data):
        break
    elif  re.search("/s",data):
        break
    else:
        print("Valid password")
        x = False
        break
if x :
    print("invalid password")'''

# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'roots'
#     )

#     if conn.is_connected():
#         print("connected")
# except Exception as obj:
#     print(obj)

# conn.close()

# ''import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host ='localhost',
#         user = 'root',
#         password = 'roots',
#         database = 'codeyug'    
#     )
#     if conn.is_connected():
#         print("connected")
# except :
#     print("Cannot connect")
# cur = conn.cursor()
# sql = '''
#      INSERT INTO tutorial(id,name,views,watchtime)
#      VALUES(107,'java basics',2435,22)
# ''' 
# try:
#     cur.execute(sql)
#     conn.commit()
#     cur.execute("DESC tutorial")
#     print("Successfully inserted ")
#     print(f'{cur.rowcount} rows inserted')
# except:
#     conn.rollback()
#     print("Something went wrong")

# cur.close()
# conn.close()

def sum_of_list(lists):
    if len()