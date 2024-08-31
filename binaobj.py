from tkinter import *
root=Tk()


def showmsg():
    print("this is msg")

btn=Button(root,text="Close me", command=quit)
btn.pack()

btn1 = Button(root, text="Show Msg", command=showmsg)
btn1.pack()
root.mainloop()
