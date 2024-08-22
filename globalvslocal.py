x=10  #global
z=20
def testvalue():
    x=5 #local
    global y
    y=10
    z=50
    print("local x=",x)
    print("local z=", z)
    s=globals()['z']
    print("localaccess global=",s)


testvalue()

print("Global x=",x)
print(y)