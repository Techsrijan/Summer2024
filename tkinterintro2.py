from tkinter import *
def msg():
    print("hi")


root=Tk()
root.title("My Window")

btn=Button(root,text="Click Me1",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"),command=msg)
btn.pack(side=TOP)


root.geometry("600x600+400+200")
root.resizable(0,0)
root.mainloop()