# 100971729 Rami Shafik

# Part 1
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Unknown")
        self.age = kwargs.get("age", 0)
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

# Testing
john = Person(age=10)
print(john.get_details())

mary = Person(name="Mary")
print(mary.get_details())

smith = Person(name="Smith", age=55)
print(smith.get_details())

# Part 2
class Employee(Person):
    def __init__(self, name, age, position, salary):
        super().__init__(name=name, age=age)
        self.position = position
        self.salary = salary
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}"

# Testing
jones = Employee("Jones Adam", 29, "Chief Executive Officer", 100_000_000)
print(jones.get_details())

# Part 3
class RentalProperty:
    def calculate_rent(self, *args):
        if len(args) < 2:
            return "At least two arguments required."
        elif len(args) == 2:
            return sum(args)
        elif len(args) == 3:
            return sum(args)
        else:
            return "Too many arguments provided."

# Testing
rent_obj = RentalProperty()
print(rent_obj.calculate_rent(700))
print(rent_obj.calculate_rent(700, 200))
print(rent_obj.calculate_rent(700, 200, 100))
print(rent_obj.calculate_rent(700, 200, 100, 998)) 

# Part 4
class Car:
    def move(self):
        return "The car accelerates and drives."

class Bicycle:
    def move(self):
        return "The bicycle pedals and moves."

def start_trip(obj):
    print(obj.move())

# Testing
ford = Car()
start_trip(ford)

bic_obj = Bicycle()
start_trip(bic_obj)