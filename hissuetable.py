import sqlite3
connection = sqlite3.connect("patient_details.db")
cursor = connection.cursor()

sqlcmd="CREATE TABLE hissue(hissue VARCHAR(30));"
cursor.execute(sqlcmd)