from doctest import SkipDocTestCase


class car:
    wheels=4

    def __init__(self):
        self.mil=16
        self.com="Skoda"


car1=car()
car2=car()

print(car1.mil,car1.com)
print(car2.mil,car2.com,car.wheels)
        
     
