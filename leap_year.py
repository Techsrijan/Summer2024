y=int(input("Enter any year"))
print(y)
if y%100==0:
    if y%400==0:
        print("leap year")
    else:
        print("not leap")
elif y%4==0:
    print("leap year")
else:
    print("not leap")