class ClassName:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    #def method_name (self):

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start (self):
        print (f"The {self.color} {self.make} {self.model} is starting")
    
    def drive (self):
        print (f"The {self.color} {self.make} {self.model} is driving")

my_car = Car ("Toyota", "Camary", "red")

my_car.start()
my_car.drive()

your_car = Car ("BMW", "S3", "blue")
your_car.start()
your_car.drive()

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print (f"{self.name} says woof")

dog1 = Dog ("Buddy", "Golden retriever")

dog1.bark()

#needs init if there are attributes (most of the time)

class Calculator:
    def add (self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
calc = Calculator()
print (calc.add (1,2))
print (calc.sub(1, 2))