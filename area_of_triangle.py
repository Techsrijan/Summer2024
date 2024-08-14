from math import *
a=int(input("Enter the first side of triangle"))
b=int(input("Enter the second side of triangle"))
c=int(input("Enter the third side of triangle"))
s=(a+b+c)/2
print("s=",s)
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle=",area)