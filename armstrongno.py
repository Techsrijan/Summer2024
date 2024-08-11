num=int(input("enter any number "))
print(num)
orig=num
sum=0
while num>0:
    a=num%10
    sum=sum+a*a*a
    num=num//10
print("sum=",sum)
if sum==orig:
    print("armstrong no")
else:
    print("not armstrong no")