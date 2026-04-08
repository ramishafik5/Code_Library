# 100971729 Rami Shafik

from abc import ABC, abstractmethod

# Part 1
class Appliance(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def turn_on(self):
        pass

# Testing Part 1
try:
    app_obj = Appliance("Generic")
except TypeError as i:
    print(i)

# Part 2
class ElectronicAppliance(Appliance):
    def turn_on(self):
        return "The electronic appliance is powered on"

class ManualAppliance(Appliance):
    def turn_on(self):
        return "This manual appliance has been powered on with a button"

# Testing Part 2
laptop = ElectronicAppliance("Laptop")
print(laptop.turn_on())

stove = ManualAppliance("Stove")
print(stove.turn_on())

# Part 3
class Telephone(ABC):
    @abstractmethod
    def use(self):
        pass

class Blackberry(Telephone):
    def use(self):
        return "Blackberry has defined the interface's abstract method"

class Iphone(Telephone):
    def use(self):
        return "Iphone has defined the interface's abstract method"

# Testing Part 3
z10 = Blackberry()
print(z10.use())

iphone8 = Iphone()
print(iphone8.use())

# Part 4
class Appliance(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    def turn_on(self):
        return "The appliance is powered on"

class ComputerAppliance(Appliance):
    def turn_on(self):
        print(super().turn_on())
        print("The computer appliance is powered on - Take 2")

class HomeAppliance(Appliance):
    def turn_on(self):
        print(super().turn_on())
        print("This home appliance has been powered on with a button - Take 2")

# Testing Part 4
mouse = ComputerAppliance("Mouse")
mouse.turn_on()

print("\n")

pot = HomeAppliance("Pot")
pot.turn_on()
