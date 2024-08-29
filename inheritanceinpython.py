class Room:      #base class or parent class
    def area(self,l,b):
        self.l=l
        self.b=b
        a=self.l*self.b
        print("area=",a)

class GuestRoom(Room):  # derived class or child class
    def room_type(self):
        print("This is guest Room")

# deriving a new class from the base class is known as inheritance.
# code reusability


g=GuestRoom()
g.room_type()
g.area(20,30)