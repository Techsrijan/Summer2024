from tkinter import *
from tkinter import messagebox
import pymysql
taz=Tk()
taz.title("My Hotel")
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
###### database connectivity##################################
def dbconnect():
    global con,mycursor
    con = pymysql.connect(host='localhost', user='root', db='merahotel')
    #print("Connection mil gaya")
    mycursor = con.cursor()

##### remove all widget #########
def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()

#---- main heading----------
def main_heading():
     lab = Label(taz, text="Wah Taz Hotel ", width=30,
                 bg="red", fg="black", font=("Comic Sans Ms", "40", "bold"))
     lab.grid(row=0, column=0,columnspan=6)

#--------welcome window-----
def welcomewindow():
    remove_all_widgets()
    main_heading()
    loginLabel = Label(taz, text="Welcome Window", font="Arial 20")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)


# admin login window
usernameVar=StringVar()
passwordVar=StringVar()
def admin_login():
    main_heading()
    loginLabel = Label(taz, text="Admin Login", font="Arial 20")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username", font="Arial 15")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    userNameEntry = Entry(taz, font="Arial 15", textvariable=usernameVar)
    userNameEntry.grid(row=2, column=2, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password", font="Arial 15")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    passwordEntry = Entry(taz, font="Arial 15",  textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    btnLogin = Button(taz, text="Login", font="Arial 15", fg="green", command=adminLoginProcess)
    btnLogin.grid(row=4, column=1, padx=20, pady=5, columnspan=2)

#--- login check process------
def adminLoginProcess():
    a = usernameVar.get()
    b = passwordVar.get()
    print(a, b)
    if a == '' or b == '':
        messagebox.showerror(title="User Credential Error", message="Please Fill Both Username and Password!!!")
    else:
        user = usernameVar.get()
        pwd = passwordVar.get()
        dbconnect()
        que = "select * from login_info where binary userid=%s and binary pwd=%s"
        val = (user, pwd)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        # print(data)
        flag = False
        for row in data:
            flag = True

        con.close()
        if flag == True:
            welcomewindow()
            # messagebox.showinfo(message='login successful')

        else:
            messagebox.showerror(title="Login Error", message="Either USerName or Password is Incorrect")
            usernameVar.set('')
            passwordVar.set('')


#print(w,h)
#taz.geometry("600x800+120+120")
taz.geometry("%dx%d+0+0"%(w,h))
main_heading()
admin_login()
taz.mainloop()