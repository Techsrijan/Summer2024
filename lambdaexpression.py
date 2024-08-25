from functools import reduce
def add(x,y):
    return (x+y)

print(add(5,6))

def even(n):
    return n%2==0

'''
a function can take any no of arguments
but have only one expression in his body
'''

f=lambda x,y:x+y

print(f(4,5))

l=[2,4,6,3,5,666,22,55,567,897,44,33]

even_no=list(filter(lambda n:n%2==0,l))
print(even_no)

data=list(map(lambda n:n+10,even_no))
print(data)

result=reduce(lambda x,y:x+y,data)
print(result)