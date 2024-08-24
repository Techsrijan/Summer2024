from turtle import *

import random
t=Turtle()

l=['red','green','yellow','blue','orange']

for i in range(100):
    t.forward(i)
    t.left(34)
    t.pencolor(l[i%5])
    t.pensize(i%20)

done()
