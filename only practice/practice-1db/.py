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
import mysql.connector
try:
    db = mysql.connector.connect(
        host= "localhost",
        user="root",
        password = "roots",
        database="codeyug1"
    )

    if db.is_connected():
        print("Connected!")

except Exception as obj:
    print("Not connected")

cur = db.cursor()

sql = "SELECT * FROM tutorial1"



try:
    cur.execute(sql)
    data = cur.fetchall()
    for ele in data:
        print(ele)
    for ele in data:
        print(ele)
    print(list(data))   
    print(f"{len(data)} rows got fetched") 
    db.commit()
    print()

except:
    db.rollback()
    print("Something went wrong")

cur.close()
db.close()


