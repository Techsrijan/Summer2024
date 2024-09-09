from tkinter import *
import pymysql
from tkinter import messagebox

conn=pymysql.connect(host="localhost",db="facebook",user="root")
print("Database connected")
mycursor=conn.cursor()

root=Tk()
def get_data():
    name=getname.get()
    age=getage.get()
    print(name,age)
    que = "insert into techsrijan(name,age)values(%s,%s)"
    val=(name,age)
    mycursor.execute(que,val)
    conn.commit()
    j.set('Data Saved')
    messagebox.showinfo(title="Data Save Message",message="Record Saved")
    getname.set('')
    getage.set('')

root.title("My Calculator")
root.iconbitmap("calci.ico")
lbl2=Label(root,font=("Comic Sans Ms",10,"bold"),
          text="Enter Your Name",fg="white",bg="black")
lbl2.place(x=50,y=50)
getname=StringVar()
ent2=Entry(root,font=("Comic Sans Ms",10,"bold"),textvariable=getname,width=30)
ent2.place(x=250,y=50)

lbl=Label(root,font=("Comic Sans Ms",10,"bold"),
          text="Enter Your Age",fg="white",bg="black")
lbl.place(x=50,y=100)
getage=IntVar()
ent=Entry(root,font=("Comic Sans Ms",10,"bold"),textvariable=getage,width=30)
ent.place(x=250,y=100)
btn=Button(root,text="Save Record",fg="red",bg="yellow",
           command=get_data)
btn.place(x=200,y=200)


j=StringVar()
lbl1=Label(root,font=("Comic Sans Ms",10,"bold"),textvariable=j
         )
lbl1.place(x=200,y=300)
k=StringVar()
ent1=Entry(root,font=("Comic Sans Ms",10,"bold"),textvariable=k)
ent1.place(x=200,y=400)

root.geometry("600x600+200+200")
root.resizable(0,0)
root.mainloop()