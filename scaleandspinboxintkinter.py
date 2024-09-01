from tkinter import *

root=Tk()
def get_data():
   print(sc.get())
   print(sp.get())

sc=Scale(root,from_=200,to=500,orient=HORIZONTAL,
         length=200,sliderlength=60,width=50)
sc.set(250)
sc.pack()

sp=Spinbox(root,from_=1,to=5,state="readonly")

sp.pack()

btn=Button(root,text="get data",command=get_data).pack()
root.geometry("400x500+120+120")
root.mainloop()