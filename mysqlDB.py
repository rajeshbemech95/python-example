import mysql.connector

database = mysql.connector.connect(
    host = "localhost", #127.0.0.1 something.domain.com
    user = "root",
    password = "",
    # port = 3306,
    # db = "costomer"
)

# print(database)
# cursor operation
c = database.cursor()
# c.execute("CREATE DATABASE costomer")
# print(database)
# c.execute("SHOW DATABASES")
# for i in c:
#     print(i)
# c.execute("CREATE TABLE shop \
#           (name VARCHAR(30), \
#            address VARCHAR(100), \
#            mobileno INT(12))")
query = "INSERT INTO shop (name,address,mobileno) VALUES(%s,%s,%s)"
value = [
         ("name1","chennai",9876),
         ("name1","chennai",9876),
         ("name1","chennai",9876),
         ("name1","chennai",9876),
         ("name1","chennai",9876),
         ("name1","chennai",9876)
         ]
         
c.executemany(query,value)
database.commit()

