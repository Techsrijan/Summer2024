from math import *
a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))
d=b*b-4*a*c
if d==0:
    print("Roots are real and equal")
    x1=x2=-b/(2*a)
    print("X1=",x1,"X2=",x2)
elif d>0:
    print("Roots are real and unequal")
    x1=(-b+sqrt(d))/(2*a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("X1=", x1, "X2=", x2)
else:
    print("roots are imaginary")