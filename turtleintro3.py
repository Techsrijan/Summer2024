from turtle import *
t=Turtle()
sc=Screen()
#sc.bgcolor('yellow')
sc.bgpic('test.gif')
sc.setup(800,600)
# t.penup()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.pd()
t.pu()
t.goto(100,100)
t.pd()
for i in range(4):
    t.forward(100)
    t.left(90)

t.reset()
t.backward(200)
for i in range(4):
    t.forward(100)
    t.left(90)
done()