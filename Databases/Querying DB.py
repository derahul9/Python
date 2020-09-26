import psycopg2

try:
    connection = psycopg2.connect(database="staff", user= "rahul", password = "7oct1991", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("connection successful!")

cursor = connection.cursor()

# cursor.execute("select * from mystaff.employees where salary > 20000;")
cursor.execute("select * from mystaff.employees where last_name like '%Richard%';")
# cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
# cursor.execute("select * from mystaff.employees where department in ('Sales', 'IT');")

#records = cursor.fetchall()

#for record in records:
#    print(record)

#records1 = cursor.fetchone()

#for record in records1:
#    print(record)

records2 = cursor.fetchmany(size = 2)

for record in records2:
    print(record)