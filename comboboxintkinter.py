from tkinter import *
from tkinter import ttk

root=Tk()
def get_data():
    print(com.get())
l=[]
#l=['UP',"Bihar",'MP',"AP"]
for i in range(1900,2025):
    l.append(i)
com=ttk.Combobox(root,value=l,height=5,state="readonly",width=4)
com.set('Year')
com.pack()

btn=Button(root,text="print combobox value",command=get_data).pack()
root.geometry("400x500+120+120")
root.mainloop()