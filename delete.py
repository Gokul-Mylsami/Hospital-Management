import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import datetime
import sqlite3
import os
connection=sqlite3.connect("patient_details.db")
cursor=connection.cursor()

def delete():
    def delinfo():
        print(strid.get())
        sqcmd="DELETE FROM details WHERE Id='{}'".format(strid.get())
        cursor.execute(sqcmd)
        connection.commit()
        win.destroy()
        win1=tk.Tk()
        tk.Label(win1,text="DELETE SUCCSSFULLY").grid(row=0,column=0)
        win1.mainloop()

    win=tk.Tk()
    l1=tk.Label(win,text="Enter the ID :")
    l1.grid(row=0,column=0)
    strid=tk.StringVar()
    e1=tk.Entry(win,width=30,textvariable=strid)
    e1.grid(row=0,column=1)

    b1=tk.Button(win,text="Delete Data !",command=delinfo)
    b1.grid(row=1,column=1)
    win.mainloop()
if __name__ == '__main__':
    print("hi")
    delete()