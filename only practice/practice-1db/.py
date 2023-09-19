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
import mysql.connector
try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password="roots",
        database="codeyug"
    )

    if conn.is_connected():
        print("connected")
except Exception as obj:
    print(obj)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS tutorial(
    video_id INT PRIMARY KEY,
    video_name VARCHAR(100) NOT NULL,
    video_views INT,
    watchtime FLOAT
)""")  
cur.execute("DESC tutorial")
for data in cur:
    print(data[0])  
conn.commit()
cur.close()
conn.close()



