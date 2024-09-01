from tkinter import *
from tkinter import simpledialog
root=Tk()
def open_meesage():
    sum=0
    for i in range(5):
        s=simpledialog.askfloat(title="Enter Marks",
                              prompt="Enter the marks of student")
        sum=sum+s
    print(sum)


btn=Button(root,text="open Simple dialog  box",command=open_meesage).pack()
root.geometry("400x500+120+120")
root.mainloop()