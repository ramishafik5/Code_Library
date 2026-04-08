#Question 5: Multiple Inheritance & Method Resolution Order

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        pass

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def get_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Department: {self.department}")

m = Manager("Alice", 35, "E123", "HR")
m.get_info()
        