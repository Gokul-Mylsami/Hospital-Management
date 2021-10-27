import sqlite3
connection = sqlite3.connect("patient_details.db")
cursor = connection.cursor()

sqlcmd="CREATE TABLE details(Id VARCHAR(20) PRIMARY KEY,Name VARCHAR(30),Fname VARCHAR(30),mno VARCHAR(15));"

cursor.execute(sqlcmd)