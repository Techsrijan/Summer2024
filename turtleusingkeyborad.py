from turtle import *
sc=Screen()
t=Turtle()
sc.title("Indian flag")

sc.listen()
def movefd():
    t.fd(100)

def movebd():
    t.backward(100)

def moveup():
    t.left(90)
    t.fd(100)


def movedown():
    t.right(90)
    t.fd(100)

sc.onkey(movebd,'B')
sc.onkey(movefd,'Up')
sc.onkey(moveup,'Left')
sc.onkey(movedown,'Right')
done()