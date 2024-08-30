from tkinter import *
root=Tk()
def leftclick(event):
    print("Left Button is clicked")

def rightclick(event):
    print("Right Button Is clicked")

def middleclick(event):
    print("Middle Button is clicked")

root.bind("<Control-l>",leftclick)
root.bind("<Control-r>",rightclick)
root.bind("<Control-m>",middleclick)
btn1=Button(root,text="Left click",fg="red",bg="yellow",
            )
btn1.pack()

btn2=Button(root,text="Right click",fg="red",bg="yellow",
            )
btn2.pack()

btn3=Button(root,text="Middle click",fg="red",bg="yellow",
            )
btn3.pack()


btn1.bind("<Button-1>",leftclick)
btn2.bind("<Button-3>",rightclick)
btn3.bind("<Button-2>",middleclick)

root.geometry("500x600+200+200")

root.resizable(0,0)
root.mainloop()