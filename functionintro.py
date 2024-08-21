

#function definition
def greet():
    print("Good morning")

greet()


def GabbuPuncherWala(puncher_cycle):
    print("Pahaiya kholo")
    print("Hawabharo")
    print("puncher check karo")
    print("repair puncher")
    print("Pahiya bhad do")

#function call
GabbuPuncherWala("sandeep")
greet()
#GabbuPuncherWala()


def calsum(x,y): # here x and y are called formal argument
    c=x+y
    print("sum=",c)

calsum(2,5)
a=int(input("Enter the first no"))
b=int(input("Enter the second no"))
calsum(a,b) # here a and b are called actual argument

# actual argument value copied into fromal argument
greet()

def sub(x,y):
    d=x-y
    return d

s=sub(55,12)
print("Ghatane ke bad=",s)

def calculator(x,y):
    d=x-y
    e=x+y
    f=x*y
    g=x/y
    return d,e,f,g

s,t,u,v=calculator(78,6)
print(s,t,u,v)