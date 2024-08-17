from array import *
# blank array
marks=array('i',[])
n=int(input("How many students do u have in a class"))
print(n)
for i in range(0,n):
    x=int(input("enter the marks of student"))
    marks.append(x)
print(marks)

#print(min(marks))

maxi=marks[0]
pos=0
for i in range(1,n):
    if maxi<marks[i]:
        maxi=marks[i]
        pos=i

print("Maximum marks=",maxi,"position=",pos+1)

search=int(input("Enter the item u want to find"))
for i in range(0,n):
    if search==marks[i]:
        print("Item found at location=",i+1)
        break
else:
    print("item not found")