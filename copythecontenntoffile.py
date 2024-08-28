f=open("college.txt","r")
f2=open("College2.txt","w")

for data in f:
    f2.write(data)