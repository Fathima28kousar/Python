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

