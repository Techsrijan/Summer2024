from tkinter import *
from tkinter import filedialog

root=Tk()
current_open_file=''
def open_file(event=''):
    op=filedialog.askopenfile(initialdir="/",title="Open File",
                           filetypes=(("Text FILE","*.txt"),("All FILE","*.*")))
    print(op)
    current_open_file=op
    for data in op:
        #print(data)
        txt.insert(INSERT,data)

def saveas_file():
    fp = filedialog.asksaveasfile(title="Save File", mode="w")
    data = txt.get(1.0, END)
    fp.write(data)

def save_file():
    if current_open_file=='':
        saveas_file()
    else:
        data = txt.get(1.0, END)
        current_open_file.write(data)
    #print(fp)

main_menu=Menu(root)
root.config(menu=main_menu)

root.bind("<Control-o>",open_file)
#creating file menu
file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",accelerator="Ctrl+N",command=open)
file_menu.add_command(label="Open",accelerator="Ctrl+o",command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save",accelerator="Ctrl+S",command=save_file)
file_menu.add_command(label="Save As",command=saveas_file)
file_menu.add_command(label="Exit",command=quit)
#creating edit menu
edit_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",accelerator="Ctrl+c")



txt=Text(root,width=15,wrap=WORD,padx=10,pady=10,selectbackground='red')
txt.pack(fill=BOTH,expand=1)

#txt.insert(INSERT,"Hello welcome you ")


root.geometry("800x600+150+150")
root.mainloop()