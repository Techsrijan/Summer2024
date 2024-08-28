'''
class variable
instance variable
'''

class Car:
    wheel=4
    def car_info(self):
        self.name='Maruti'  # instance variable
        self.mil=50
        print("Name=",self.name,"Milage=",self.mil)


c1=Car()
c1.car_info()
c1.mil=500
print(c1.wheel)
c1.car_info()
c2=Car()
print(Car.wheel)
Car.wheel=45
print(Car.wheel)