n=int(input("enter any number"))
i=2
while i<=n-1:
    if n%i==0:
        print("Not Prime")
    else:
        print("Prime no")
        break
    i=i+1