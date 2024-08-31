from tkinter import *

class Mywindow:
    def showmsg(self):
        print("this is msg")

    def __init__(self,window):  #constructor
       self.btn=Button(window,text="Close me", command=quit)
       self.btn.pack()

       self.btn1 = Button(window, text="Show Msg", command=self.showmsg)
       self.btn1.pack()

root=Tk()
ob=Mywindow(root)
root.mainloop()