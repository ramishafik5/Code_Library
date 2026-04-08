class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)


class Math:
    def add(self, *args):
        return sum(args)
    
m = Math()
print(m.add(5, 10))
print(m.add(1, 2, 3, 4))
#position matters for args


def add_numbers(*args):
    print(args)
    return sum(args)

result = add_numbers(1, 2, 5)
print(result)


print("S1" + "S2")
print("S1"+ str(12))


def greet(greeting, *names):
    for name in names:
        print(f"{greeting} {names}!")

greet("Hello", "Alice", "Peter", "Bob")


numbers = [1, 2, 3]
print(*numbers)


class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pertending to be a duck!")

def make_it_quack(thing):
    thing.quack()

make_it_quack(Duck())
make_it_quack(Person())


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

car = Car()
car.start_engine()


class Appliance(ABC):
    @abstractmethod
    def operate(self):
        pass

class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes")

class Microwave(Appliance):
    def operate(self):
        print("Heating food")

wm = WashingMachine()
mw = Microwave()
wm.operate()
mw.operate()


class Product:
    def __init__(self, name, price, *args, **kwargs):
        self.name = name
        self.price = price

    def display_info(self):
        return f"Prodcut: {self.name}, Price: ${self.price}"
    
class Laptop(Product):
    def __init__(self, name, price, ram, storage, *args, **kwargs):
        super().__init__(name, price, *args, **kwargs)
        self.ram = ram
        self.storage = storage

    def display_info(self):
        return f"Laptop: {self.name}, Price: ${self.price}, RAM: {self.ram}, Storage: {self.storage}"
    
class Smartphone(Product):
    def __init__(self, name, price, camera_megapixels, *args, **kwargs):
        super().__init__(name, price, *args, **kwargs)
        self.camera_megapixels = camera_megapixels

    def display_info(self):
        return f"Smartphone: {self.name}, Price: ${self.price}, Camera: {self.camera_megapixels}"
    
def print_product_details(product):
    print(product.display_info())

laptop = Laptop("Dell", 1200, 16, 512)
smartphone = Smartphone("iPhone", 999, 12)

print_product_details(laptop)
print_product_details(smartphone)

def operate(device):
    print(device.display_info())

operate(laptop)
operate(smartphone)


class Calculator:
    def add(self, *args):
        return sum(args)
    
calc = Calculator()
print("Addition (2 args)", calc.add(5, 10))
print("Addition (4 args)", calc.add(1, 5, 2, 3))


print(len("Hello World"))
print(len([1, 2, 3, 4, 5, 6]))
print(len({"a": 1, "b":2}))