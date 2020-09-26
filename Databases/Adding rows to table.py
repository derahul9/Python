import psycopg2

# select * from mystaf.employees - To see if there are any rows in the table

try:
    connection = psycopg2.connect(database="staff", user= "rahul", password = "7oct1991", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("connection successful!")

cursor = connection.cursor()

# Adding Rows to the DB:

cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) \
 values (1, 'John', 'Smith', 'Sales', '0123456789', '1st Street, Miami', 50000), \
        (2, 'Jack', 'Doe', 'IT', '0213456742', '2nd Street, NY', 55000), \
        (3, 'Emily', 'Davids', 'Sales', '0123456999', '3rd Street, LA', 59000), \
        (4, 'Karen', 'Willson', 'Logistics', '0823556785', '4th Street, Las Vegas', 41000), \
        (5, 'Emma', 'Richard', 'Marketing', '0423453580', '5th Street, Denver', 40000);")

connection.commit()

connection.close()

# Updating a Row:

cursor = connection.cursor()
cursor.execute("update mystaff.employees set department = 'Logistics' where last_name = 'Doe';")
connection.commit()
# connection.rollback() - Can be used to rollback the last commit
connection.close()