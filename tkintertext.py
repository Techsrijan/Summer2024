from tkinter import *
root=Tk()

def get_data():
    data=txt.get(1.0,END)
    print(data)

def delete_data():
    result=txt.selection_get()
    print(result)
    loc=txt.search(result,1.0,stopindex=END)
    print(loc)
    txt.delete(loc)

def clear_data():
    txt.delete(1.0, END)


main_menu=Menu(root)
root.config(menu=main_menu)

#creating file menu
file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",accelerator="Ctrl+N",command=open)
file_menu.add_command(label="Open",accelerator="Ctrl+o")
file_menu.add_separator()
file_menu.add_command(label="Save",accelerator="Ctrl+S")
file_menu.add_command(label="Save As")

#creating edit menu
edit_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",accelerator="Ctrl+c")



txt=Text(root,width=15,wrap=WORD,padx=10,pady=10,selectbackground='red')
#txt.pack(fill=BOTH,expand=1)
txt.pack()
txt.insert(INSERT,"Hello welcome you ")
btn=Button(root,text="Get txt Data",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"),command=get_data)
btn.pack()

btndel=Button(root,text="Get delete Data",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"),command=delete_data)
btndel.pack()

btnclear=Button(root,text="clear Data",fg="red",bg="yellow",
           font=("Comic sans Ms",15,"bold"),command=clear_data)
btnclear.pack()
root.geometry("800x600+150+150")
root.mainloop()