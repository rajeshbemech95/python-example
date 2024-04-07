import mysql.connector

# establishing connection
database = mysql.connector.connect(
    host = "localhost" ,#127.0.0.1 , 
    user = "root",
    port = "3306",
    passwd = "",
    database = "employee"
    )
print("connection has been established")
print(database)

#staerts the cursor operation
cursorObject =  database.cursor()

#create table

# employeeRecord = '''CREATE TABLE record(
#                     NAME VARCHAR(20) NOT NULL,
#                     DEPARTMENT VARCHAR(20),
#                     EMPLOYEE_ID INT,
#                     DOB INT
#                     )'''
sql = "INSERT INTO EMPLOYEE (NAME, DEPARTMENT, EMPLOYEE_ID, DOB)" #VALUES(%s , %s, %d,%d)"
       # VALUES(%s , %s, %d,%d)"
val = ("Hello","HR",1234, 1505)
    #    ("Hello","HR",1234, 1505),
    #    ("Hello","HR",1234, 1505),
    #    ("Hello","HR",1234, 1505),
    #    ("Hello","HR",1234, 1505)
       

# create database
cursorObject.execute(sql,val)
database.commit()

#
database.close()


