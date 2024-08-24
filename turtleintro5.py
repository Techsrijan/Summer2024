from turtle import *
import time
screen=Screen()
t=Turtle()
screen.setup(420,320)
#screen.bgpic('bg.gif')
t.shape('turtle')
t.color('darkgoldenrod','black')
s=10
t.pu()
t.setpos(30,30)
t.pd()
t.write("\u0915\u092C\u0942\u0924\u0930",font=(25))
#t.write("abcd",font=("Comic Sans Ms",25,"bold"))
for i in range(28):
        s=s+2
        #t.stamp()
        t.dot()
        t.pu()
        t.forward(s)
        t.pd()
        t.right(25)
        time.sleep(1)



'''
from turtle import *
t=Turtle()
t.shape('turtle')
for i in range(5):
    t.forward(50)
    t.stamp()
done()'''