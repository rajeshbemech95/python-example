import mysql.connector
val1 = input("val1")
val2 = input("val2")
val3 = input("val3")
#connect to db
dataBase = mysql.connector.connect(
            host = "localhost",
            user = "root",
            port = 3306,  
            passwd = "",
            database = "student"
)
print("db connected....")
cursorObject = dataBase.cursor()

sql = "INSERT INTO STUDENT(NAME, ROLL, AGE) \
        VALUES (%s , %s, %s)"
val = (val1, val2, val3)

cursorObject.execute(sql, val)
dataBase.commit()
dataBase.close()