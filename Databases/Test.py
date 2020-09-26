import psycopg2

#postgresql is installed by default in Python. Use sudo -i -u postgres to switch account to postgres. Type psql to enter sql prompt
# create database staff; To create database and to check it use \l
# create user rahul with encrypted password '7oct1991'; To create username password and \du to check the same
# grant all privileges on database staff to rahul;
# By default you are connected to database postgres, \c staff rahul to connect to your database
# create schema mystaff authorization rahul; To create a schema and to check it use \dn
# drop schema mystaf; drop user rahul; drop database staff;
# To check if table is created - \dt mystaff.*

try:
    connection = psycopg2.connect(database="staff", user= "rahul", password = "7oct1991", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("connection successful!")

cursor = connection.cursor()

# creating table employees in mystaff scheme
cursor.execute('''create table mystaff.employees
                    (id int primary key not null,
                     first_name varchar(25) not null,
                     last_name varchar(25) not null,
                     department varchar(25) not null,
                     phone varchar(25),
                     address varchar(25),
                     salary int);''')

connection.commit()

connection.close()
