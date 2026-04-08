class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print (f"{self.make} {self.model}'s engine has started")

my_car = Car("Toyota", "Supra")
my_car.start_engine()


class Example:
    def __init__(self, value):
        self.value = value

obj1 = Example(10)
onj2 = Example(20)


class Example:
    class_attribute = "Shared"

obj1 = Example()
obj2 = Example()

print(obj1.class_attribute, obj2.class_attribute)
Example.class_attribute = "Updated"
print(obj1.class_attribute, obj2.class_attribute)


class Car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print (car1.wheels, car1.brand, car1.model)
print (car2.wheels, car2.brand, car2.model)
Car.wheels = 5
print (car1.wheels, car2.wheels)


class Example:
    def method(self):
        return "Instance method"
    
obj = Example()
print(obj.method())


class Example:
    @classmethod
    def method(cls):
        return "Class method"
    
print (Example.method())


class Counter:
    count = 0 

    @classmethod
    def increment (cls):
        cls.count += 1
        return cls.count
    
print (Counter.increment())
print (Counter.increment())


class Example:
     @staticmethod
     def method():
         return "Static method"
     
print (Example.method())


class MathUntils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
print(MathUntils.add(1, 2))
print(MathUntils.multiply (2, 3))


class MathUntils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def info(cls):
        return f"This is {cls.__name__}"
    
print (MathUntils.add(3, 5))
print (MathUntils.info())
    

def function():
    return "Function"

class Example:
    def method(self):
        return "Method"

obj = Example()


class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"
    
greeter = Greeter("Sam")

print (greeter.greet())


class MathOperations:
    operation_count = 0

    def add (a, b):
        return a + b
    
    @classmethod
    def get_operation_count(cls):
        cls.operation_count += 1
        return cls.operation_count
    
    @staticmethod
    def is_even(a):
        if a % 2 == 0:
            return "Is even"
        else:
            return "Is odd"
    
print (MathOperations.add(1, 2))
print (MathOperations.get_operation_count())
print (MathOperations.get_operation_count())
print (MathOperations.get_operation_count())
print (MathOperations.is_even(3))