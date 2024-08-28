bipin=open("college.txt","a")
print(bipin)
# print(bipin.read())
#
# for i in bipin:
#     print(i)

data=input("Enter your text")
#print(data)

bipin.write(data)

bipin.close()
f=open("college.txt","r")
print(f.read())