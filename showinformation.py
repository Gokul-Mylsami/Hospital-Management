import tkinter as tk
from tkinter import *
import tkinter.font as font
import datetime
import sqlite3
import os
connection=sqlite3.connect("patient_details.db")
cursor=connection.cursor()

def mainpage():
    def showdata():
        t_details = []
        sqcmd = "pragma table_info(details)"
        cursor.execute(sqcmd)
        result = cursor.fetchall()
        for i in result:
            t_details.append(i[1])

        c_details = []
        cursor.execute("SELECT * FROM details WHERE Id='{}'".format(strid.get()))
        res = cursor.fetchall()
        j = 0
        for i in res:
            c_details.append(i)

        issue = []
        cursor.execute("SELECT * FROM hissue")
        r = cursor.fetchall()
        for i in r:
            issue.append(i[0])
        try:
            f=open("details.doc","w")
            f.write("          ID "+ " : "+ c_details[0][0]+"\n")
            f.write("          NAME"+" : "+c_details[0][1]+"\n")
            f.write("   Father-Name"+" : "+c_details[0][2]+"\n")
            f.write(" Mobile-Number"+" : "+c_details[0][3]+"\n")
            f.write(" Date-of-Birth"+" : "+c_details[0][4]+"\n")
            f.write("   BLOOD GROUP"+" : "+c_details[0][5]+"\n")
            f.write("     AADHAR NO"+" : "+c_details[0][6]+"\n\n")
            j=0
            f.write("-------------------------------------------------")
            for i in range(7, len(t_details), 2):
                if c_details[0][i]==None:
                    pass
                else:
                    f.write("\nHealth Issue   :" + issue[j] + "\n")
                    f.write("Description    :"+c_details[0][i]+"\n")
                if c_details[0][i + 1]==None:
                    pass
                else:
                    f.write("Date           :"+ c_details[0][i + 1]+"\n")
                j = j + 1
            f.close()
            os.system("details.doc")
        except:
                 win=tk.Tk()
                 tk.Label(win,text="Details not Found !").grid(row=0,column=0)
                 win.mainloop()

    win=tk.Tk()
    l1=tk.Label(text="Enter ID :")
    l1.grid(row=0,column=0)
    strid=StringVar()
    e1=tk.Entry(width=35,textvariable=strid)
    e1.grid(row=0,column=1)
    b1=tk.Button(text="Get Details",command=showdata)
    b1.grid(row=1,column=1)
    win.mainloop()



if __name__ == '__main__':
    mainpage()