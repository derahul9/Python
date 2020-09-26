import psycopg2

# select * from mystaf.employees - To see if there are any rows in the table

try:
    connection = psycopg2.connect(database="staff", user= "rahul", password = "7oct1991", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("connection successful!")

# Updating a Row:
cursor = connection.cursor()
cursor.execute("update mystaff.employees set department = 'Logistics' where last_name = 'Doe';")


# Deleting a Row:

cursor.execute("delete from mystaff.employees where salary > 50000;")
connection.commit()
connection.close()