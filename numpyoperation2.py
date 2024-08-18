from numpy import *

a=array([[1,2,3],
        [4,5,6],
        [7,8,9],
        [3,5,7]]
        )

print(a)
print(a.shape)
print(a.size)
print(a.dtype)
print(diagonal(a))
print(a.flatten())
#print(a.reshape(2,3,2))


b=array([[1,2,3],
        [4,5,6],
        [7,8,9],
        ]
        )

#print(a+b)
print(a@b)
print(dot(a,b))