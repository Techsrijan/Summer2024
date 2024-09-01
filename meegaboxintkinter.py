from tkinter import *
from tkinter import messagebox
root=Tk()
def open_meesage():
     result=messagebox.askyesno(title="Save Dialog box",
                                message="Do You want to save this file?")
     print(result)
     if result==True:
         print("file is saved")
     else:
         quit()
    # result = messagebox.showerror(title="Save Dialog box",
    #                              message="Do You want to save this file?")
btn=Button(root,text="open message box",command=open_meesage).pack()
root.geometry("400x500+120+120")
root.mainloop()
