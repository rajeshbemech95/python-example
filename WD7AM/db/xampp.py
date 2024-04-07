import mysql.connector

database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = ""
)
cursorobj = database.cursor()


cursorobj.execute("CREATE DATABASE student")

database.close()