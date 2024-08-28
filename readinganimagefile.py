f=open("test.gif","rb")
print(f)
f2=open("best.gif","wb")
for i in f:
    print(i)
    f2.write(i)