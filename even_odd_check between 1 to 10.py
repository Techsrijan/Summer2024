'''

a=1
while a<=10:
    #print(a)
    if a % 2 == 0:
        print("even no=", a)
    else:
        print("Odd no=", a)
    a=a+1'''

start=int(input("enter the start number"))
last=int(input("enter the last number"))
a=start
even_sum=0
odd_sum=0
even_mul=1
odd_mul=1
while a<=last:
    #print(a)
    if a % 2 == 0:
        even_sum=even_sum+a
        even_mul=even_mul*a
        print("even no=", a)
    else:
        odd_sum=odd_sum+a
        odd_mul=odd_mul*a
        print("Odd no=", a)
    a=a+1
print("Even sum=",even_sum,"even mul=",even_mul)
print("Odd sum=",odd_sum,"odd mul=",odd_mul)

