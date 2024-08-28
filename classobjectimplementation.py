class Student:  # user defined class
    def student_info(self):
        print("This is student detail")

s=Student() # creating student class object
Student.student_info(s)

# what is self--self is the object of its class

s.student_info()