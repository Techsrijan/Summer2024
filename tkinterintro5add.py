from tkinter import *
root=Tk()
def get_data():
    a=int(i.get())
    b=int(p.get())
    t=a+b
    j.set(t)
    k.set(t)
    i.set('')
    p.set('')

def sub_data():
    a = int(i.get())
    b = int(p.get())
    t = b-a
    j.set(t)
    k.set(t)
    i.set('')
    p.set('')
root.title("My Calculator")
root.iconbitmap("calci.ico")
lbl2=Label(root,font=("Comic Sans Ms",10,"bold"),
          text="Enter Any Number",fg="white",bg="black")
lbl2.place(x=50,y=50)
p=StringVar()
ent2=Entry(root,font=("Comic Sans Ms",10,"bold"),textvariable=p,width=30)
ent2.place(x=250,y=50)

lbl=Label(root,font=("Comic Sans Ms",10,"bold"),
          text="Enter Any Number",fg="white",bg="black")
lbl.place(x=50,y=100)
i=StringVar()
ent=Entry(root,font=("Comic Sans Ms",10,"bold"),textvariable=i,width=30)
ent.place(x=250,y=100)
btn=Button(root,text="ADD",fg="red",bg="yellow",
           command=get_data)
btn.place(x=200,y=200)

btn1=Button(root,text="Sub",fg="red",bg="yellow",
           command=sub_data)
btn1.place(x=300,y=200)
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