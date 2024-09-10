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


#---billgenerationwindow------
def billgenerationwindow():
    pass

#---- logout------
def adminLogout():
    remove_all_widgets()
    admin_login()

#-----back button
def backButtonf():
    remove_all_widgets()
    welcomewindow()
#---- update item-----
def updateItem():
    pass

#--add item
def addItem():
    name=itemnameVar.get().upper()
    rate=itemrateVar.get()
    type=itemTypeVar.get().title()
    #print(name,rate,type)
    if name=='' or rate=='' or type=='':
        messagebox.showerror("Add Item Error", "Please fill all Details")
    else:
        dbconnect()
        queins="insert into itemlist(item_name,item_rate,item_type)values(%s,%s,%s)"
        val=(name,rate,type)
        mycursor.execute(queins, val)
        con.commit()
        messagebox.showinfo("Item Added"," Item Iserted Suucessfully")
        itemnameVar.set('')
        itemrateVar.set('')
        itemTypeVar.set('')
# --- delete item--
def deleteItem():
    pass
#----additemwindow----

itemnameVar=StringVar()
itemrateVar=StringVar()
itemTypeVar=StringVar()
def additemwindow():
    remove_all_widgets()
    main_heading()
    welcomeitemLabel = Label(taz, text="Item Details", font="Arial 20")
    welcomeitemLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    ###############################
    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backButtonf)
    billButton.grid(row=1, column=0)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=adminLogout)
    logoutButton.grid(row=1, column=3)

    ###########################
    ###########################

    itemnameLabel = Label(taz, text="Item name")
    itemnameLabel.grid(row=2, column=1, padx=20, pady=5)

    itemrateLabel = Label(taz, text="Item Rate")
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type")
    itemTypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=2, padx=20, pady=5)
    #itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    #itemrateEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables validation

    itemTypeEntry = Entry(taz, textvariable=itemTypeVar)
    itemTypeEntry.grid(row=4, column=2, padx=20, pady=5)

    updateButton = Button(taz, text="UpDate Item", width=20, height=2, fg="green", bd=10, command=updateItem)
    updateButton.grid(row=6, column=0)

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10, command=addItem)
    additemButton.grid(row=6, column=1, columnspan=2)

    deleteButton = Button(taz, text="Delete Item", width=20, height=2, fg="green", bd=10, command=deleteItem)
    deleteButton.grid(row=6, column=3)
#----password change -----------
def password_change():
    a=usernameVar1.get()
    b =oldpassword.get()
    c=passwordVar1.get() #new
    d=passwordVar2.get() #reenter

    if a=='' or b=='' or c=='' or d=='':
        messagebox.showerror(title="Change Password Error", message="Please Fill All Details!!!")
    elif c==d:
        dbconnect()
        #print(c, a, b)
        quecheck='select * from  login_info where userid=%s and pwd=%s'
        val1 = (a,b)
        mycursor.execute(quecheck, val1)
        result = mycursor.fetchone()
        if result==None:
            messagebox.showerror(title="Change Password Error", message="Password Not changed")
            passwordVar1.set('')
            passwordVar2.set('')
            oldpassword.set('')
            usernameVar1.set('')
        else:
            que = "update login_info set pwd=%s where userid=%s and pwd=%s"
            val = (c, a, b)
            mycursor.execute(que, val)
            con.commit()
            messagebox.showinfo(title="Change Password Message", message="Password changed successfully")
            passwordVar1.set('')
            passwordVar2.set('')
            oldpassword.set('')
            usernameVar1.set('')
    else:
        messagebox.showerror(title='New and Renter Password Error',message="New Password and Re enter Password does not Match")

        passwordVar1.set('')
        passwordVar2.set('')
#--*---change password---
usernameVar1=StringVar()
passwordVar1=StringVar()
passwordVar2=StringVar()
oldpassword=StringVar()
def change_pass():
    remove_all_widgets()
    main_heading()
    loginLabel = Label(taz, text="Change Password", font="Arial 20")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)
    backButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backButtonf)
    backButton.grid(row=2, column=0)

    UserIdLabel = Label(taz, text="User ID", font="Arial 15")
    UserIdLabel.grid(row=2, column=1, padx=20, pady=5)

    UserIdEntry = Entry(taz, font="Arial 15", textvariable=usernameVar1)
    UserIdEntry.grid(row=2, column=2, padx=20, pady=5)

    oldpasswordLabel = Label(taz, text="Old Password", font="Arial 15")
    oldpasswordLabel.grid(row=3, column=1, padx=20, pady=5)

    oldpasswordEntry = Entry(taz, font="Arial 15", textvariable=oldpassword)
    oldpasswordEntry.grid(row=3, column=2, padx=20, pady=5)

    newpasswordLabel = Label(taz, text="New Password", font="Arial 15")
    newpasswordLabel.grid(row=4, column=1, padx=20, pady=5)

    newpasswordEntry = Entry(taz, font="Arial 15", textvariable=passwordVar1)
    newpasswordEntry.grid(row=4, column=2, padx=20, pady=5)

    renewpasswordLabel = Label(taz, text="Re-enter Password", font="Arial 15")
    renewpasswordLabel.grid(row=5, column=1, padx=20, pady=5)

    renewpasswordEntry = Entry(taz, font="Arial 15", textvariable=passwordVar2)
    renewpasswordEntry.grid(row=5, column=2, padx=20, pady=5)

    btnLogin = Button(taz, text="Change Password", font="Arial 15", fg="green",command=password_change)
    btnLogin.grid(row=6, column=1, padx=20, pady=50, columnspan=10)


#--------welcome window-----
def welcomewindow():
    remove_all_widgets()
    main_heading()
    loginLabel = Label(taz, text="Welcome Window", font="Arial 20")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)
    additemButton = Button(taz, text="Manage Restaurant", width=20, height=2, fg="green", bd=10, command=additemwindow)
    additemButton.grid(row=2, column=0)

    billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10,
                        command=billgenerationwindow)
    billButton.grid(row=2, column=1)

    changePwdBtn = Button(taz, text="Change password",width=20, height=2, fg="green", bd=10, command=change_pass)
    changePwdBtn.grid(row=2, column=2,)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=adminLogout)
    logoutButton.grid(row=2, column=3)

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
    #print(a, b)
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