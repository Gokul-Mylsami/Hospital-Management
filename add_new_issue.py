import  tkinter as tk
from tkinter import font as font
from tkinter import *
from tkinter import ttk
import sqlite3
import os
connection=sqlite3.connect("patient_details.db")
cursor=connection.cursor()

def submit():
    print(strhiss.get())
    sqcmd = "ALTER TABLE details ADD '{}' VARCHAR(30)".format("des" + strhiss.get())
    cursor.execute(sqcmd)
    sqcmd = "ALTER TABLE details ADD '{}' VARCHAR(30)".format("date" + strhiss.get())
    cursor.execute(sqcmd)
    sqcmd = "INSERT INTO hissue VALUES('{}')".format(strhiss.get())
    cursor.execute(sqcmd)
    connection.commit()
    print("Tables Altered")
    add_new_win.destroy()

add_new_win = tk.Tk()
l1 = tk.Label(add_new_win, text="Enter the new Health Issue :")
l1.grid(row=0, column=0)
strhiss = StringVar()
e1 = tk.Entry(add_new_win, width=30, textvariable=strhiss)
e1.grid(row=0, column=1)
b1 = tk.Button(add_new_win, text="Submit", command=submit)
b1.grid(row=1, column=1)
add_new_win.mainloop()
