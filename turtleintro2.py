from turtle import *
t=Turtle() # built in class
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.fd(100)

def myshape():
    t.forward(100)
    t.left(90)
# for i in range(4):
#     t.forward(100)
#     t.left(90)
t.pensize(10)
for i in range(1,5):
    if i%2==0:
        t.color('red')
        #myshape()
        t.forward(100)
        t.left(90)
    else:
        t.color('green')
        # myshape()
        t.forward(100)
        t.left(90)

done()