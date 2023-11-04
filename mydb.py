import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'AP31bc4326@'
)

cursorObject = dataBase.cursor() 


cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")