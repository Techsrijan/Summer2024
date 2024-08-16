from array import *

p,q=50,66
print(id(p))
print(id(q))
s=50
print(id(s))


a=array('f',[1121,33,66.66,33,55,44,66,33])
print(a)

k=0
while k<len(a):
    print(a[k])
    k=k+1

print(len(a))
'''
x=int(input("Enter the item u want to count "))
print(a.count(x))
if a.count(x)==0:
    print("Item not found")
else:
    print(a.count(x))
'''
for i in a:
    print(i)

for i in range(0,len(a)):
    print(a[i])

x=array('i',[1,2,3,4,5])
y=array('i',[1,2,3,4,5])

print(x+y)

print(x.append(10))
print(x)

print(a.typecode)
print(a.reverse())
print(a)
print(a.buffer_info())

