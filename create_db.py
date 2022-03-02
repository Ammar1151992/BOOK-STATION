import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ammarh1151992",
)

my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE db_books")
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)