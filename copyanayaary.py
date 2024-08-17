from numpy import *
#aliasing same address
# change of one affects other
a=array([1,2,3,4,5])
b=a
print(a,id(a))
print(b,id(b))
b[2]=8000
print(b,id(b))
print(a,id(a))

# shallow copy
# different address
# change of one affects other
x=array([10,66,99,44])
y=x.view()
print(x,id(x))
print(y,id(y))
y[2]=9266
print(x,id(x))
print(y,id(y))

#deep copy
# different address
# change of one not affects other
p=array([33,66,99,65])
q=p.copy()
print(p,id(p))
print(q,id(q))
q[2]=9266
print(p,id(p))
print(q,id(q))
