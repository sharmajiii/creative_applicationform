import hojo

import pymysql
from tkinter import *
from tkinter import messagebox
import mysql.connector


connection = pymysql.connect(host='localhost',user='root',password='root',db='bank')
cursor=connection.cursor()

sql = "INSERT INTO bank(fn,mn,ln,an,pa,pn,em,gn) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
try:
    
    cursor.execute(sql,(hojo.app[0],hojo.app[1],hojo.app[2],hojo.app[3],hojo.app[4],hojo.app[5],hojo.app[6],hojo.app[7]))
    print("successsul")
    class tjj:
        def __init__(self):
            window=Tk()
            window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
            window.withdraw()
            messagebox.showinfo('CONGRATULATION!!!','DATA HAS BEEN RECORDED  :)')
            window.deiconify()
            window.destroy()
            window.quit()
    if __name__ == '__main__':
            tjj()


except:
    import rr
#result=cursor.fetchall()
connection.commit()
    
    





