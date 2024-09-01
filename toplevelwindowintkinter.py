from tkinter import *

root=Tk()
def open_window():
    t=Toplevel(root)
    t.title("Child window")
    btn1 = Button(t, text="close window", command=t.destroy)
    btn1.pack()
    t.geometry("400x500+120+120")
btn2=Button(root,text="open window",command=open_window).pack()
btn3=Button(root,text="close window",command=quit).pack()
root.geometry("400x500+120+120")
root.mainloop()
