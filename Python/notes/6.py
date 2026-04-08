class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)

p3 = Point(5, 7)
p4 = Point(3, 4)
print(p3 - p4)

p5 = Point(1, 2)
p6 = Point(1, 2)
print (p5 == p6)


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(c1 + c2)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade
    
s1 = Student("Alice", 90)
s2 = Student("Bob", 30)

print (s1 == s2)
print (s1 > s2)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
p = Person("john", 30)
print (str(p))
print (repr(p))


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
obj1 = Singleton()
obj2 = Singleton()
print (obj1 is obj2)


class Car:
    def drive(slef):
        pass

class Sedan(Car):
    def drive(self):
        return "Driving a Sedan"
    
class SUV(Car):
    def drive(self):
        return "driving a SUV"
    
class CarFactory:
    @staticmethod
    def get_car(car_type):
        if car_type == "Sedan":
            return Sedan()
        elif car_type == "SUV":
            return SUV()
        
car = CarFactory.get_car("SUV")
print(car.drive())


class EruopeanPlug:
    def connect(self):
        return "Connected to European socket"
    
class USPlug:
    def connect_to_US_socket(self):
        return "Connected to US socket"
    
class Adapter:
    def __init__(self, plug):
        self.plug = plug

    def connect(self):
        return self.plug.connect_to_US_socket()
    
plug = USPlug()
adapter = Adapter(plug)
print (adapter.connect())


class Observer:
    def update(self, message):
        pass

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received {message}")

class NotificarionSystem:
    def __init__(self):
        self.observers = []

    def add_observers(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

user1 = User("Alice")
user2 = User("Bob")
system = NotificarionSystem()
system.add_observers(user1)
system.add_observers(user2)
system.notify("New Message!")


import unittest

'''class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqaul(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()'''


'''class Calculator:
    def add(sefl, a, b):
        return a + b
    
class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0) 

if __name__ == "__main__":
    unittest.main()'''


from unittest.mock import MagicMock

class API:
    def get_data(self):
        return "Real data"
    
api = API
api.get_data = MagicMock(return_value = "Mocked data")

print(api.get_data())


import logging

logging.basicConfig(level = logging.DEBUG)
logging.debug("This is a debug message")