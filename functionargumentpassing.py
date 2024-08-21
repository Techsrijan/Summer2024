'''
We can pass value inside function by four methods
1. postional arguments
2. keyword argument
3  variable length argument
4. keyword variable length argument
'''

#1. postional arguments
def person(name,age):
    age=age+15
    print("name=",name,"age=",age)

person("ashwani",55)
#person(55,"dsadas")

#2. keyword argument

person(name="abcd",age=545)
person(age=6565,name="sdfdsf")

#3  variable length argument
def add(*y):
    #print(x)
    #print(*y,type(y))
    sum=0
    for i in y:
        sum=sum+i
    return sum
print(add(40,50,5,6565))

'''
t=(1,2,3,4,5)
sum=0
for i in t:
    sum=sum+i
    print(i)
print(sum)'''

#4. keyword variable length argument
def persondata(**data):
    print(data)
    for i, j in data.items():
        print(i, j)

persondata(name="ashwani",age=55,mo='9956477677',city='gkp',marks=566,adhar=456646466)
