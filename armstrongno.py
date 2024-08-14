i=1
while i<=1000:
    num = i
    #print(num)
    orig = num
    sum = 0
    while num > 0:
        a = num % 10
        sum = sum + a * a * a
        num = num // 10
    #print("sum=", sum)
    if sum == orig:
        print("armstrong no=",orig)
    else:
        #print("not armstrong no")
        pass
    i=i+1
