#protected attributes should start with _, can be accessed in sub classes
#private attributes should start with __, cannot be accessed in sub classes

class Person:
    def __init__(self, name):
        self._name = name

person = Person ("Alice")
print (person._name)


class BankAccount:
    def __init__(self,):
        self.__balance = 1000

account = BankAccount()
#or
class BankAccount:
    def __init__(self, balance = 1000):
        self.__balance = balance

account = BankAccount()
#print (account.__balance) #will make an error

#_className__attribute shows private attributes 
print (account._BankAccount__balance)


#Parent class = super class = base class
#Child class = sub class = Derived class

class Parent:
    def __init__(self):
        self.__data= "Parent's data"

class Child (Parent):
    def __init__(self):
        super().__init__()
        self.__data = "Child's data"

obj = Child() #sub class has parent class attributes
print (obj._Parent__data)
print (obj._Child__data)


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print ("Invaled balance value")

account = BankAccount(500)
print (account.get_balance())
account.set_balance(1000)
print (account.get_balance())
account.set_balance(-100)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"
    #end user friendly
    
    def __repr__(self):
        return f"Person ('{self.name}', {self.age})"
    #developer friendly 


class Book:
    def __init__(self, author, title):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book (title = {self.title}, author = {self.author})"
    
book = Book ("George Orwell", "1984")

print (book)
print (str(book))
print (repr(book))

class Book:
    def __init__(self, author, title):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book (title = {self.title}, author = {self.author})"
    
book = Book ("George Orwell", "1984")

print (repr(book))


#<__main__.Book object at 0x7f5srdhhjgv>


class Book:
    def __init__(self, title, author, is_signed_out):
        self.title = title
        self.author = author
        self.__is_signed_out = is_signed_out