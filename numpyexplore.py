from numpy import *
'''
There are six ways to create an array using numpy
1.array()
2.linspace
3.logspace
4.arange
5.zeros
6.ones
'''

a=array([1,2,3,4,5])
print(a)
print(type(a))

b=linspace(1,50)
print(b)

c=logspace(1,50)
print(c)

d=arange(1,15,2)
print(d)

z=zeros(10)
print(z)

one=ones(100)
print(one)