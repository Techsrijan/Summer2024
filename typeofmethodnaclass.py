'''
types of methods in class
1. instance method ---which accepts self as argument
2. class method -- which accepts cls as argument
3. static method - which accepts no argument
'''

class Training:
    schoolname='Techsrijan'
    # instance method
    def getmarks(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        return self.m1 + self.m2 + self.m3

    #class method
    @classmethod    #decorator
    def get_school_name(cls):
        return cls.schoolname

    #static method
    @staticmethod
    def run_without_argument():
        print("I will not take any argument")

print(Training.get_school_name())
Training.run_without_argument()
s=Training()
print(s.getmarks(10,20,30))


