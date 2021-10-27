import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import datetime
import sqlite3
import os
connection=sqlite3.connect("patient_details.db")
cursor=connection.cursor()


class mainpage():

    def mainpagefun(self):
        def showinformation():
            win.destroy()
            os.system("showinformation.py")
        def updateinfo():
            def newinfo():
                update_info_win.destroy()
                os.system('newinfo.py')
            def delete():
                update_info_win.destroy()
                os.system("delete.py")
            def updinfo():
                update_info_win.destroy()
                os.system('updateinfo.py')
            win.destroy()
            update_info_win=tk.Tk()
            update_info_win.geometry("1024x720")
            update_info_win.title('Update Information')
            my_font = font.Font(family="Comic Sans MS", size=29, weight="bold")
            button_font = font.Font(family="Courier", size=17)
            l0 = tk.Label(update_info_win,text="                                                                                                 ")
            l0.grid(row=0, column=0)
            l1=tk.Label(update_info_win,text="Update Information\n")
            l1['font']=my_font
            l1.grid(row=0,column=1)

            # buttons
            b1=tk.Button(update_info_win,text="New Information" ,command=newinfo)
            b1['font']=button_font
            b1.grid(row=2,column=1)

            tk.Label(update_info_win,text="\n").grid(row=3, column=1)

            b2=tk.Button(update_info_win,text="Update Information",command=updinfo)
            b2['font']=button_font
            b2.grid(row=4,column=1)

            tk.Label(update_info_win, text="\n").grid(row=5, column=1)

            b3=tk.Button(update_info_win,text="Delete Information ",command=delete)
            b3['font']=button_font
            b3.grid(row=6,column=1)



            update_info_win.mainloop()

        win = tk.Tk()
        win.title("Hospital Management")
        win.geometry("1024x720")
        button_font = font.Font(family="Courier",size=17)
        my_font = font.Font(family="Comic Sans MS", size=29, weight="bold")
        l0=tk.Label(win,text="                                                                                                 ")
        l0.grid(row=0,column=0)
        l1=tk.Label(win,text="Hospital Management\n")
        l1['font'] = my_font
        l1.grid(row=0,column=1)
        b1 = tk.Button(text="Update Information" , command=updateinfo)
        b1['font']=button_font
        b1.grid(row=1, column=1)
        tk.Label(text="\n").grid(row=2,column=1)
        b2 = tk.Button(text="Show Information",command=showinformation)
        b2['font']=button_font
        b2.grid(row=3,column=1)

        win.mainloop()

if __name__ == "__main__":
    m1 = mainpage()
    m1.mainpagefun()