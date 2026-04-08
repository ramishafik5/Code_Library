#100971729 Rami Shafik

#creating class
class Vehicle:

    #creating the attributes for the class
    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer
        self.total_seats = 5
        self.occupied_seats = 0
        self.occupying_seats = []
        print (f"Model: {self.model}, Manufacrurer: {self.manufacturer}")
        
    #function to show the number of availble seats    
    def get_free_seats(self):
        return self.total_seats - self.occupied_seats

    #function to remove a person from the list    
    def unoccupy_seats (self):
        if len(self.occupying_seats) >= 1:
            self.occupying_seats.pop()
            self.occupied_seats -= 1
    
    #function to add someone to the list
    def occupy_seats (self, name):
        if self.get_free_seats() > 0:
            self.occupying_seats.append (name)
            self.occupied_seats += 1

    #function to clear all seast
    def clear_all_seats(self):
       del self.occupying_seats [:]
       self.occupied_seats = 0

#set class as a veriable 
ford = Vehicle("Ford V1", "Ford")

#test the functions in the class
print(ford.get_free_seats())
ford.occupy_seats ("Sandra")
ford.occupy_seats ("Paul")
print(ford.get_free_seats())

ford.unoccupy_seats()
print (ford.get_free_seats())

ford.occupy_seats ("John")
print (ford.get_free_seats())
ford.clear_all_seats()
print (ford.get_free_seats())