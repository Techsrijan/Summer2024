from tkinter import *
root=Tk()
can=Canvas(root,width=600,height=400,bg="yellow")
# line=can.create_line(0,0,400,400)
# line2=can.create_line(100,100,200,300)
# rec=can.create_rectangle(100,100,200,300,width=30,fill="blue",
#                          outline="red")
# #cir=can.create_oval(150,150,60,60,fill="green")
# oval=can.create_oval(200,200,100,50,fill="red")
# arc=can.create_arc(150,150,60,60,start=0,extent=90,fill="green")
#txt=can.create_text("vipin")
point=[200,110,480,200,280,280,200,110]
poly=can.create_polygon(point,fill="green")
# photo=PhotoImage(file="best.gif")
# can.create_image(10,10,image=photo,anchor=CENTER)
can.pack()
root.geometry("600x600+120+200")
root.mainloop()
