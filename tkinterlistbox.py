from tkinter import *
root=Tk()
root.title("My Window")
def get_data():
    select_item=l.curselection()
    print(select_item)
    for i in select_item:
        print(l.get(i))
def delete_data():
    select_item = l.curselection()
    print(select_item)
    for i in select_item:
        print(l.delete(i))

def insert_data():
    data=j.get()
    l.insert(END,data)

f=Frame(root)


# scroll bar
scroll=Scrollbar(f)
scroll.pack(side=RIGHT,fill=Y)



# BROWSE SINGLE MULTIPLE EXTENDED
l=Listbox(f,height=10,width=20,yscrollcommand=scroll.set,
          selectmode=EXTENDED)
# l.insert(0,'abcd')
# l.insert(1,'xyz')
for i in range(20):
    l.insert(i,i+1)
l.pack()
scroll.config(command=l.yview)
f.pack()
j=StringVar()
ent=Entry(root,textvariable=j,)
ent.pack(pady=10)

btnins=Button(root,text="insert List Data",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"),command=insert_data)
btnins.pack()


btn=Button(root,text="Get List Data",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"),command=get_data)
btn.pack()

btn2=Button(root,text="delete list data",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"),command=delete_data)
btn2.pack()
root.geometry("600x600+400+200")
root.resizable(0,0)
root.mainloop()