import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font
import datetime
import sqlite3
import os
connection=sqlite3.connect("patient_details.db")
cursor=connection.cursor()
date_object = datetime.date.today()
health_issues = []
sqcmd = "SELECT * FROM hissue"
cursor.execute(sqcmd)
result = cursor.fetchall()
for i in result:
    health_issues.append(i[0])

def mainsc():

    def addnew():
        os.system("add_new_issue.py")
    def refresh():
        update_info_win.destroy()
        health_issues.clear()
        sqcmd = "SELECT * FROM hissue"
        cursor.execute(sqcmd)
        result = cursor.fetchall()
        for i in result:
            health_issues.append(i[0])
        mainsc()

    def submitupdateinfo():
        try:
            sqcmd="UPDATE details SET '{}' = '{}' WHERE Id='{}'".format("des"+strhissue.get(),strdes.get(),strid.get())
            cursor.execute(sqcmd)
            sqcmd = "UPDATE details SET '{}' = '{}' WHERE Id='{}'".format("date"+strhissue.get(), date_object,strid.get())
            cursor.execute(sqcmd)
            connection.commit()
            update_info_win.destroy()
            newwin=tk.Tk()
            l0=tk.Label(newwin,text="Successfully Updated !")
            l0.grid(row=1,column=1)
            newwin.mainloop()
        except:
            update_info_win.destroy()
            newwin = tk.Tk()
            l0 = tk.Label(newwin, text=" ID does not exist !")
            l0.grid(row=1, column=1)
            newwin.mainloop()
        update_info_win.destroy()
    update_info_win = tk.Tk()
    update_info_win.geometry("1024x720")
    update_info_win.title("Update Information:")

    text_font = font.Font(family="sans-serif", size=18)

    topicframe = Frame(update_info_win)
    topicframe.grid(row=0, column=0)
    tk.Label(topicframe, text="                ").grid(row=0, column=0)
    l0 = tk.Label(topicframe, text="Update Information :")
    my_font = font.Font(family="Comic Sans MS", size=29, weight="bold")
    l0['font']=my_font
    l0.grid(row=1,column=1)
    tk.Label(text="\n").grid(row=2,column=1)

    l1=tk.Label(update_info_win,text="ID :")
    l1['font']=text_font
    l1.grid(row=3,column=1)

    strid=StringVar()
    e1=tk.Entry(update_info_win,width=32,textvariable=strid)
    e1.grid(row=3,column=2)

    l5 = tk.Label(update_info_win, text="Health-Issue :")
    l5['font'] = text_font
    l5.grid(row=5, column=1)

    strhissue = tk.StringVar()
    c1 = ttk.Combobox(update_info_win, width=32, textvariable=strhissue)
    c1['values'] = health_issues
    c1.grid(row=5, column=2)

    b1 = tk.Button(update_info_win, text="Add-New", command=addnew)
    b1.grid(row=5, column=4, padx=30)

    b2 = tk.Button(update_info_win, text="Refresh", command=refresh)
    b2.grid(row=5, column=5)

    l6 = tk.Label(update_info_win, text="Description :")
    l6['font'] = text_font
    l6.grid(row=6, column=1)

    strdes = tk.StringVar()
    e6 = tk.Entry(update_info_win, width=35, textvariable=strdes)
    e6.grid(row=6, column=2)

    b3 = tk.Button(update_info_win, text="Submit", command=submitupdateinfo)
    b3.grid(row=7, column=2)

    update_info_win.mainloop()

if __name__ == '__main__':
    mainsc()