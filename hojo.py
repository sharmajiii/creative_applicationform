import sys
from tkinter import filedialog
import PIL.Image
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
#import yy
from PIL import ImageTk, Image
top= Tk()
top.geometry("1047x892+502+254")
top.title("SHARMAJI APPLICATION DATABASE FORM")
top.configure(relief="groove")
top.configure(background="#d9d9d9")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")
a=StringVar()
b =StringVar()
c =StringVar()
d =IntVar()
e =StringVar()
f =IntVar()
g =StringVar()
h =StringVar()
def quit():
     global top
     top.destroy()
def submt():
     global app
     app=['m','n','o','p','q','r','s','t']
     app[0] = a.get()
     app[1] = b.get()
     app[2] = c.get()
     app[3] = d.get()
     app[4] = e.get()
     app[5] = f.get()
     app[6] = g.get()
     app[7] = h.get()
     quit()

def file():
        n =Entry7.get()
        f = filedialog.askopenfilename(
         parent=top, initialdir='C:/Tutorial',
        title='Choose file',
        filetypes=[('png images', '.png'),
                           ('gif images', '.gif'), ("jpeg", "*.jpg")]

        )
        hii(f, n)
def hii(self,name):
        img = Image.open(self).resize((150, 150), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)  # type: Any
        img.save( name + ".png")
        print(name)
        Frame6 = Label(top, image=image)
        Frame6.image = image
        Frame6.place(relx=0.38, rely=0.10, relheight=0.19, relwidth=0.16)
        Frame6.configure(relief=SUNKEN)
        Frame6.configure(borderwidth="2")
        Frame6.configure(relief=SUNKEN)
        Frame6.configure(background="#d9d9d9")
        Frame6.configure(highlightbackground="#d9d9d9")
        Frame6.configure(highlightcolor="black")
        Frame6.configure(width=331)

#frames lables and widgts
Frame1 = Frame(top)
Frame1.place(relx=0.16, rely=0.0, relheight=0.77, relwidth=0.18)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="2")
Frame1.configure(relief=GROOVE)
Frame1.configure(background="SeaGreen2")
Frame1.configure(width=185)

Labelframe1 = LabelFrame(Frame1)
Labelframe1.place(relx=1.19, rely=0.31, relheight=0.11, relwidth=0.81)
Labelframe1.configure(relief=GROOVE)
Labelframe1.configure(foreground="black")
Labelframe1.configure(text='''Labelframe''')
Labelframe1.configure(background="slate blue")
Labelframe1.configure(width=150)
Frame7 = Frame(Frame1)
Frame7.place(relx=-1.41, rely=0.82, relheight=0.11, relwidth=0.68)
Frame7.configure(relief=GROOVE)
Frame7.configure(borderwidth="2")
Frame7.configure(relief=GROOVE)
Frame7.configure(background="#d9d9d9")
Frame7.configure(width=125)

Frame2 = Frame(top)
Frame2.place(relx=0.0, rely=0.0, relheight=0.77, relwidth=0.17)
Frame2.configure(relief=GROOVE)
Frame2.configure(borderwidth="2")
Frame2.configure(relief=GROOVE)
Frame2.configure(background="medium slate blue")
Frame2.configure(width=185)

Frame3 = Frame(top)
Frame3.place(relx=0.33, rely=0.0, relheight=0.77, relwidth=0.18)
Frame3.configure(relief=GROOVE)
Frame3.configure(borderwidth="2")
Frame3.configure(relief=GROOVE)
Frame3.configure(background="light slate blue")
Frame3.configure(width=185)

Frame4 = Frame(top)
Frame4.place(relx=0.5, rely=0.0, relheight=0.77, relwidth=0.18)
Frame4.configure(relief=GROOVE)
Frame4.configure(borderwidth="2")
Frame4.configure(relief=GROOVE)
Frame4.configure(background="slate blue")

Frame5 = Frame(top)
Frame5.place(relx=0.67, rely=0.0, relheight=0.77, relwidth=0.18)
Frame5.configure(relief=GROOVE)
Frame5.configure(borderwidth="2")
Frame5.configure(relief=GROOVE)
Frame5.configure(background="SeaGreen2")
Frame5.configure(width=185)

Button1 = Button(top,command=submt)
Button1.place(relx=0.50, rely=0.69, height=50, width=130)
Button1.configure(text='''SUBMITT''')
Button1.configure(background="peach puff")

Label11 = Label(top)
Label11.place(relx=0.4, rely=0.03, height=36, width=150)
Label11.configure(background="peach puff")
Label11.configure(foreground="DarkOrchid1")
Label11.configure(relief=SUNKEN)
Label11.configure(text='''APPLICATION FORM''')

Label2 = Label(top)
Label2.place(relx=0.01, rely=0.09, height=36, width=112)
Label2.configure(highlightbackground="#d9d9d9")
Label2.configure(relief=RAISED)
Label2.configure(text='''FIRST NAME''')

Label3 = Label(top)
Label3.place(relx=0.01, rely=0.16, height=36, width=112)
Label3.configure(relief=RAISED)
Label3.configure(text='''MIDDLE NAME''')

Entry1 = Entry(top,textvar=a)
Entry1.place(relx=0.15, rely=0.09,height=34, relwidth=0.19)

Entry2 = Entry(top,textvar=b)
Entry2.place(relx=0.15, rely=0.15,height=34, relwidth=0.19)

Label4 = Label(top)
Label4.place(relx=0.01, rely=0.22, height=36, width=112)
Label4.configure(relief=RAISED)
Label4.configure(text='''LAST NAME''')

Label6 = Label(top)
Label6.place(relx=0.01, rely=0.355, height=36, width=110)
Label6.configure(relief=RAISED)
Label6.configure(text='''GENDER''')

Label7 = Label(top)
Label7.place(relx=0.01, rely=0.44, height=36, width=110)
Label7.configure(relief=RAISED)
Label7.configure(text='''AADHAR NUMBER''')

Label8 = Label(top)
Label8.place(relx=0.01, rely=0.5, height=36, width=130)
Label8.configure(relief=RAISED)
Label8.configure(text='''PERMANENT ADDRESS''')



Label9 = Label(top)
Label9.place(relx=0.01, rely=0.57, height=36, width=130)
Label9.configure(relief=RAISED)
Label9.configure(text='''PHONE MUNBER''')

Entry3 = Entry(top,textvar=c)
Entry3.place(relx=0.15, rely=0.22,height=34, relwidth=0.19)

Frame8 = Frame(top)
Frame8.place(relx=0.84, rely=0.0, relheight=0.77, relwidth=0.16)
Frame8.configure(relief=GROOVE)
Frame8.configure(borderwidth="2")
Frame8.configure(relief=GROOVE)
Frame8.configure(background="DarkOliveGreen1")
Frame8.configure(width=165)

Label0= Label(top)
Label0.place(relx=0.01, rely=0.29, height=35, width=110)
Label0.configure(relief=RAISED)
Label0.configure(text='''COUNTRY''')

TCombobox1 = ttk.Combobox(top,values=["AMERICA","BANGALDESH","CANADA","INDIA","DENMARK"])
TCombobox1.place(relx=.15, rely=0.29, relheight=0.04
                , relwidth=0.105)
TCombobox1.configure()
TCombobox1.configure(takefocus="")

Entry4 = Entry(top,textvar=d)
Entry4.place(relx=0.15, rely=0.44,height=34, relwidth=0.19)

Entry5 = Entry(top,textvar=e)
Entry5.place(relx=0.15, rely=0.5,height=34, relwidth=0.29)

Entry6 = Entry(top,textvar=f)
Entry6.place(relx=0.15, rely=0.57,height=34, relwidth=0.19)

Entry7 = Entry(top,textvar=g)
Entry7.place(relx=0.15, rely=0.65, height=34, relwidth=0.19)

Entry8 = Entry(top,textvar=h)
Entry8.place(relx=0.15, rely=0.35,height=34, relwidth=0.13)

Label11 = Label(top)
Label11.place(relx=0.01, rely=0.65, height=36, width=110)
Label11.configure(relief=RAISED)
Label11.configure(text='''EMAIL''')

Button2 = Button(top,command=file)
Button2.place(relx=0.44, rely=0.29, height=43, width=126)
Button2.configure(text='''SELECT IMAGE''')

Button2 = Button(top,command=quit)
Button2.place(relx=0.72, rely=0.57, height=43, width=126)
Button2.configure(text='''QUIT''')
Button2.configure(background="WHITE")




path="C:/Users/vipul/Desktop/lol.jpg"
img = Image.open(path).resize((2550, 550), Image.ANTIALIAS)
image = ImageTk.PhotoImage(img)  # type: Any
Frame9 = Label(top, image=image)
Frame9.image = image
Frame9.place(relx=0.0,rely=.77,height=180,width=2100)

top.mainloop()


