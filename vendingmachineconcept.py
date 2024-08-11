n=int(input("how many toffe u want"))
print(n)
stock=15
i=1
while i<=n:
    if i<=stock:
        print("Please Collect Toffe=",i)
    else:
        print("Out Of stock")
        break
    i=i+1
else: # this else will run when loop runs properly
    print("thank u Please Visit again")
