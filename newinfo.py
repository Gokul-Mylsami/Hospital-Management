import  tkinter as tk
from tkinter import font as font
from tkinter import *
from tkinter import ttk
import sqlite3
import os
import datetime

date_object = datetime.date.today()
connection=sqlite3.connect("patient_details.db")
cursor=connection.cursor()
health_issues = []
sqcmd = "SELECT * FROM hissue"
cursor.execute(sqcmd)
result = cursor.fetchall()
for i in result:
    health_issues.append(i[0])
def mainwin():

    def refresh():
        new_info_win.destroy()
        health_issues.clear()
        sqcmd = "SELECT * FROM hissue"
        cursor.execute(sqcmd)
        result = cursor.fetchall()
        for i in result:
            health_issues.append(i[0])
        mainwin()
    def addnew():
        os.system('add_new_issue.py')
    def submitnewinfo():

        if(1):
            sqcmd="INSERT INTO details (Id,Name,Fname,Mno,'{}','{}',DOB,BGROUP,AADHAR) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("des"+strhissue.get(),"date"+strhissue.get(),strid.get(),strname.get(),strfname.get(),strmno.get(),strdes.get(),date_object,strdob.get(),strbgroup.get(),strano.get())
            success_screen = tk.Tk()
            success_font=font.Font(family='sans-serif',size=19,weight='bold')
            cursor.execute(sqcmd)
            cursor.execute("COMMIT")
            connection.commit()
            l1=tk.Label(success_screen,text="Successfully Added !")
            l1['font']=success_font
            l1.grid(row=0,column=0)
            success_screen.mainloop()
            new_info_win.destroy()
        # except:
        #     l1=tk.Label(success_screen,text="Id already exist")
        #     l1['font']=success_font
        #     l1.grid(row=0,column=0)
        #     success_screen.mainloop()

    new_info_win = tk.Tk()
    new_info_win.geometry("1024x720")
    new_info_win.title("New Information")

    text_font = font.Font(family="sans-serif", size=20)

    topicframe = Frame(new_info_win)
    topicframe.grid(row=0, column=0)
    tk.Label(topicframe, text="                ").grid(row=0, column=0)
    l0 = tk.Label(topicframe, text="New Information :")
    my_font = font.Font(family="Comic Sans MS", size=29, weight="bold")
    l0['font'] = my_font
    l0.grid(row=0, column=1)

    tk.Label(topicframe, text="\n\n").grid(row=1, column=0)

    inputframe = Frame(new_info_win)
    inputframe.grid(row=1, column=1)
    # ID
    l1 = tk.Label(inputframe, text="    ID      :")
    l1['font'] = text_font
    l1.grid(row=1, column=1)

    strid = tk.StringVar()
    e1 = tk.Entry(inputframe, width=35, textvariable=strid)
    e1.grid(row=1, column=2)

    l2 = tk.Label(inputframe, text="Name    :")
    l2['font'] = text_font
    l2.grid(row=2, column=1)

    strname = tk.StringVar()
    e2 = tk.Entry(inputframe, width=35, textvariable=strname)
    e2.grid(row=2, column=2)



    l3 = tk.Label(inputframe, text="F-Name :")
    l3['font'] = text_font
    l3.grid(row=3, column=1)

    strfname = tk.StringVar()
    e3 = tk.Entry(inputframe, width=35, textvariable=strfname)
    e3.grid(row=3, column=2)

    l7=tk.Label(inputframe,text="DOB   :")
    l7['font']=text_font
    l7.grid(row=4,column=1)

    strdob=tk.StringVar()
    e7=tk.Entry(inputframe,width=35,textvariable=strdob)
    e7.grid(row=4,column=2)

    l8=tk.Label(inputframe,text="Blood Group :")
    l8['font']=text_font
    l8.grid(row=5,column=1)

    strbgroup=tk.StringVar()
    e8=tk.Entry(inputframe,width=35,textvariable=strbgroup)
    e8.grid(row=5,column=2)

    l9=tk.Label(inputframe,text="Aadhar No:")
    l9['font']=text_font

    l9.grid(row=6,column=1)

    strano=tk.StringVar()
    e9=tk.Entry(inputframe,width=35,textvariable=strano)
    e9.grid(row=6,column=2)


    l4 = tk.Label(inputframe, text="Mobile-No :")
    l4['font'] = text_font
    l4.grid(row=7, column=1)

    strmno = tk.StringVar()
    e4 = tk.Entry(inputframe, width=35, textvariable=strmno)
    e4.grid(row=7, column=2)


    l5 = tk.Label(inputframe, text="Health-Issue :")
    l5['font'] = text_font
    l5.grid(row=8, column=1)

    strhissue = tk.StringVar()
    c1 = ttk.Combobox(inputframe, width=32, textvariable=strhissue)
    c1['values'] = health_issues
    c1.grid(row=8, column=2)

    b1 = tk.Button(inputframe, text="Add-New",command=addnew)
    b1.grid(row=8, column=4, padx=30)

    b2 = tk.Button(inputframe, text="Refresh",command=refresh)
    b2.grid(row=8, column=5)

    l6 = tk.Label(inputframe, text="Description :")
    l6['font'] = text_font
    l6.grid(row=9, column=1)

    strdes = tk.StringVar()
    e6 = tk.Entry(inputframe, width=35, textvariable=strdes)
    e6.grid(row=9, column=2)

    b3 = tk.Button(inputframe, text="Submit", command=submitnewinfo)
    b3.grid(row=10, column=2)
    new_info_win.mainloop()

if __name__ == '__main__':

    mainwin()
