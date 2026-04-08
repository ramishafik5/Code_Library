# 100971729 Rami Shafik

#create class
class Car:

    #create class level attribute
    max_speed = 120

    #instance method function with the car attributes
    def __init__(self, make, model, year, price, mileage):
        self.make = make
        self.model = model
        self.year = year
        self._price = price
        self.__mileage = mileage

    #string function to return the attributes of the car 
    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.__mileage} miles, Price: ${self._price}"
    
    #function to get the model of the car
    def get_model (self):
        return self.model
    
    #function to change the model of the car
    def set_model (self, new_model):
        self.model = new_model

    #function to change price of car
    def set_price (self, new_pirce):
        if new_pirce > 0:
            self._price = new_pirce
        else:
            print ("New Price must be greater than 0.")

    #function to get mileage
    def get_mileage (self):
        return self.__mileage

    #classmethod function to get class level attribute
    @classmethod
    def get_max_speed(cls):
        return cls.max_speed
    
    #static method function to get the age of the car
    @staticmethod
    def calculate_age(year_of_manufacture):
        return 2025 - year_of_manufacture
    
# Testing the class
ford = Car("Ford", "V2", 2025, 97000, 200)
print(ford)

print(ford.get_model())
ford.set_model("V20")
print(ford.get_model())

ford.set_price(20000)
print(ford)

print(ford.get_mileage()) 

print(Car.max_speed)
print(Car.get_max_speed())

print(Car.calculate_age(1998))