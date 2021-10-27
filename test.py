import sqlite3
import os
connection=sqlite3.connect("patient_details.db")
cursor=connection.cursor()


sqcmd="ALTER TABLE details ADD AADHAR VARCHAR(30)"
cursor.execute(sqcmd)

connection.commit()