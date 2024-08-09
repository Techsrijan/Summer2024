
try:
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    div=a/b
    print("div=",div)

except ValueError:
    print("You have entered a character")
except ZeroDivisionError:
    print("B can not be zero")
except Exception:
    print("something went wrong")
finally:
    print("thank you for using my program")


'''
if True:
    #print("hi")
    pass
else:
    print("Bye")'''