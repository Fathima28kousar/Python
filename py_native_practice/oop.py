#OOP Exercise 1: Create a Class with instance attributes,,,Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.***********
'''class Vehicle:
    def __init__(self,max_speed,milaege):
        self.max_speed = max_speed
        self.milaege = milaege

model = Vehicle(240,70)
print(model.max_speed,model.milaege)       '''
#Create a Vehicle class without any variables and methods**************
'''class Vehicle:
    pass'''

class Vehicle:
    def __init__(self,max_speed,milaege):
        self.max_speed = max_speed
        self.milaege = milaege


class Bus(Vehicle):
    def vehicle_name(self):
        print("vehicle is good")

b1 = Bus()
print(b1.vehicle_name(240kmph,29))