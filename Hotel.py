from tkinter import *
from tkinter import messagebox
taz=Tk()
taz.title("My Hotel")
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()

# welcome window
def welcomewindow():
    pass

# login check
def logincheck():
    a=username.get()
    b=password.get()
    print(a,b)
    if a=='' or b=='':
        messagebox.showerror(title="User Credential Error", message="Please Fill Both Username and Password!!!")
    else:
        print("Loginho gaya")
        welcomewindow()




# def main_heading():
#     lab = Label(taz, text="Wah Taz Hotel ", width=30,
#                 bg="red", fg="black", font=("Comic Sans Ms", "40", "bold"))
#     lab.grid(row=0, column=0,columnspan=6)

# def welcome_window():
#     main_heading()


lab = Label(taz, text="Wah Taz Hotel ", width=30,
                bg="red", fg="black", font=("Comic Sans Ms", "40", "bold"))
lab.grid(row=0, column=0,columnspan=6)

lab2 = Label(taz, text="Admin Login ", width=30,
                 fg="green", font=("Comic Sans Ms", "22", "bold"))
lab2.grid(row=1, column=2)

usernameLbl=Label(taz,font=("Comic Sans Ms",15,"bold"),
          text="Enter User ID",fg="white",bg="black")
usernameLbl.grid(row=2,column=1,pady=50)


username=StringVar()
userid=Entry(taz,font=("Comic Sans Ms",10,"bold"),textvariable=username,width=30)
userid.grid(row=2,column=2,pady=50)


pwdLbl=Label(taz,font=("Comic Sans Ms",15,"bold"),
          text="Enter User Password",fg="white",bg="black")
pwdLbl.grid(row=3,column=1,pady=50)


password=StringVar()
userpwd=Entry(taz,font=("Comic Sans Ms",10,"bold"),textvariable=password,width=30)
userpwd.grid(row=3,column=2,pady=50)

btn=Button(taz,text="Login",fg="red",bg="yellow",
           command=logincheck)
btn.grid(row=4,column=2,pady=50)
#print(w,h)
#taz.geometry("600x800+120+120")
taz.geometry("%dx%d+0+0"%(w,h))
taz.mainloop()