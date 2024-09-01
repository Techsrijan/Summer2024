from tkinter import *
root=Tk()
def open():
    print("Open ho gaya")
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

root.geometry("400x500+120+120")
root.mainloop()