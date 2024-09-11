from tkinter import *
from tkinter import ttk
root=Tk()
def getData():
  print(i.get())
  if i.get()==1:
      print("Hindi")

i=IntVar()
j=IntVar()
k=IntVar()
lf=LabelFrame(root,text="Select Language Known")
r1=Checkbutton(lf,text="Hindi",variable=i)
r1.pack()
r2=Checkbutton(lf,text="English",variable=j)
r2.pack()
r3=Checkbutton(lf,text="Urdu",variable=k)
r3.pack()

lf.pack()


btn=Button(root,text="Get Data",command=getData)
btn.pack()
root.geometry("400x400+120+120")
root.mainloop()
