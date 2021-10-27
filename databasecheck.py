import sqlite3
connection=sqlite3.connect("patient_details.db")
cursor = connection.cursor()

sqcmd="SELECT * FROM details"
cursor.execute(sqcmd)

result = cursor.fetchall()

for i in result:
    print(i)