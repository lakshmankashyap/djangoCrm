import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'Lk@mysql123'
)

#prepare a cursor object
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE django_crm")

print('All Done!')