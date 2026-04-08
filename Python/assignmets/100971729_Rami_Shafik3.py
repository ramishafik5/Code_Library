#100971729 Rami Shafik

#parent class
class ElectricVehicle:

    #class level attribute
    total_robots_made = 0

    #instance method set teh values of teh attributes
    def __init__(self, cost, battery_life, producton_year, manufacturer, model_number):
        self.__cost = cost
        self._battery_life = battery_life
        self.production_year = producton_year
        self.manufacturer = manufacturer
        self.model_number = model_number

    #str methode to diaplya the cost manufacturer and model number
    def __str__(self):
        return f"Cost: {self.__cost}, Manufacturer: {self.manufacturer}, ModelNumber: {self.model_number}"
    
    #get the batter life value
    def get_battery_life(self):
        return self._battery_life
    
    #set a new cost
    def set_cost(self, new_cost):
        self.__cost = new_cost
    
    #reset all the attribute values
    def reset_robot(self):
        self.__cost = None
        self._battery_life = None
        self.production_year = None
        self.manufacturer = None
        self.model_number = None

#inherit class
class CompanyVehicle (ElectricVehicle):
    def __init__(self, cost, battery_life, producton_year, manufacturer, model_number):
        super().__init__(cost, battery_life, producton_year, manufacturer, model_number)

    #change the value of the cost attribute
    def set_cost(self, new_cost):
        if new_cost > 5000:
            self._ElectricVehicle__cost = new_cost

# Testing creation
vehicle1 = CompanyVehicle(20000, 90.5, 2020, "Tesla", "Y7")

print(vehicle1.get_battery_life())
print(vehicle1)
vehicle1.set_cost(4000) 

print(vehicle1)
vehicle1.set_cost(97000)

print(vehicle1._ElectricVehicle__cost) 

vehicle1.reset_robot() 
print(vehicle1)
print(vehicle1.get_battery_life())

        