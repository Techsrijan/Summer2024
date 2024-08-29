from tkinter import *
root=Tk()
root.title("My Window")

btn=Button(root,text="Click Me1",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"))
btn.pack(side=TOP)

btn1=Button(root,text="Click Me2",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"))
btn1.pack(side=BOTTOM,fill=X)

btn2=Button(root,text="Click Me3",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"))
btn2.pack(side=LEFT,fill=Y)

btn3=Button(root,text="Click Me4",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"))
btn3.pack(side=RIGHT)
root.geometry("600x600+400+200")
root.resizable(0,0)
root.mainloop()