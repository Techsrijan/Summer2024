from tkinter import *
def get_data():
    print(a.get())
    print(b.get())
    i=a.get()
    j=b.get()
    k=i+j
    print(k)

root=Tk()
root.title("My Window")

lbl=Label(root,text="Enter First no",fg="red",bg="yellow",
             font=("Comic sans Ms",15,"bold"))
lbl.place(x=100,y=50)
a=IntVar()
txt=Entry(root, font=("Comic sans Ms",15,"bold"),textvariable=a,bd=10,justify="right")
txt.place(x=350,y=50)

lbl1=Label(root,text="Enter Second no",fg="red",bg="yellow",
             font=("Comic sans Ms",15,"bold"))
lbl1.place(x=100,y=100)

b=IntVar()
txt1=Entry(root, font=("Comic sans Ms",15,"bold"),textvariable=b)
txt1.place(x=350,y=100)


btn=Button(root,text="Add",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"),command=get_data)
btn.place(x=400,y=200)


root.geometry("800x600+400+200")
root.resizable(0,0)
root.mainloop()