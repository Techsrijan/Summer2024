from tkinter import *
root=Tk()

def get_data():
    print(i.get())
i=StringVar()

r1=Radiobutton(root,text="Male",value='male', variable=i)
r1.pack()
r2=Radiobutton(root,text="Female",value='female',variable=i)
r2.pack()

lf=LabelFrame(root,text="Select Category")
r3=Radiobutton(lf,text="SC")
r3.pack()
r4=Radiobutton(lf,text="ST")
r4.pack()
r5=Radiobutton(lf,text="OBC")
r5.pack()
r6=Radiobutton(lf,text="GENERAL")
r6.pack()
lf.pack()
btn=Button(root,text="Get Data",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"),command=get_data)
btn.pack()
root.geometry("800x600+120+120")
root.mainloop()