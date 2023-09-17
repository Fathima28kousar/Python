import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="FKW#84#kousar", database="health")
cursor = connection.cursor()

# Check if the table 'vice' already exists
cursor.execute("SHOW TABLES LIKE 'vice'")
table_exists = cursor.fetchone()

if not table_exists:
    create_table = """
        CREATE TABLE vice(
            Hospital_Id INT UNSIGNED NOT NULL,
            name VARCHAR(32),
            bed_count INT,
            PRIMARY KEY(Hospital_Id)
        )
    """
    cursor.execute(create_table)

# Rest of your code for inserting data

cursor.close()
connection.close()
import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", password="FKW#84#kousar", database="health")
    
    if connection.is_connected():
        print("Connected to MySQL database")
        
        # The rest of your code for table creation and data insertion goes here
        
except mysql.connector.Error as error:
    print("Error: ", error)
    
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")
