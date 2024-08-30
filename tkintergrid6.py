from tkinter import *
root=Tk()
root.title("My Calculator")
root.iconbitmap("calci.ico")

lbl2=Label(root,font=("Comic Sans Ms",10,"bold"),
          text="Enter Any Number",fg="white",bg="black")
lbl2.grid(row=0,column=0,padx=10,pady=10)
p=StringVar()
ent2=Entry(root,font=("Comic Sans Ms",10,"bold"),textvariable=p,width=30)
ent2.grid(row=0,column=1)

lbl=Label(root,font=("Comic Sans Ms",10,"bold"),
          text="Enter Any Number",fg="white",bg="black")
lbl.grid(row=1,column=0)
i=StringVar()
ent=Entry(root,font=("Comic Sans Ms",10,"bold"),textvariable=i,width=30)
ent.grid(row=1,column=1)
btn=Button(root,text="ADD",fg="red",bg="yellow",
          )
btn.grid(row=2,column=0,columnspan=2)

root.geometry("500x600+200+200")

root.resizable(0,0)
root.mainloop()