class Test:
    def check(self):
        print("I will run with the help of object")
        c=self.a+self.b
        print(c)


    # this is constructor
    # it will be invocked automatically
    # when the object is created
    def __init__(self):
        print("I will run without object")
        self.a=10
        self.b=20


t=Test()
t.check()
t2=Test()