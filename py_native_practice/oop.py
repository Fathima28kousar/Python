#OOP Exercise 1: Create a Class with instance attributes,,,Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.***********
class Vehicle:
    def __init__(self,max_speed,milaege):
        self.max_speed = max_speed
        self.milaege = milaege

model = Vehicle(240,70)
print(model.max_speed,model.milaege)       