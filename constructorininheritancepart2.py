class A:
    def __init__(self):
        print("this is class A contructor")

class B(A):

    def __init__(self):
        super().__init__()
        print("this is class B contructor")



class C(B):

    def __init__(self):
        super().__init__()
        print("this is class C contructor")

ob=C()