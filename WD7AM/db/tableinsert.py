import mysql.connector

#connect to db
dataBase = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "student"
)
print("db connected....")


#preparing to edit
cursorObject = dataBase.cursor()

#insert table
studentRecord = """CREATE TABLE STUDENT(
                    NAME VARCHAR(20) NOT NULL,
                    ROLL INT NOT NULL,
                    AGE INT NOT NULL)"""
cursorObject.execute(studentRecord)
dataBase.close()

