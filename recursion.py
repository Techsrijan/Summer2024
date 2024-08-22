import sys
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(sys.getrecursionlimit()+1500))
#print(sys.getrecursionlimit())

def greeting():
    print("Good morning")



def meeting():
    greeting()
    print("at 12 O clock=")
    meeting()




meeting()