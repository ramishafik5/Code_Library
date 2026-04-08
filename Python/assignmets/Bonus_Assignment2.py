class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out (self):
        if self.__is_checked_out:
            print (f"'{self.title}' is already checked out")
        else:
            self.__is_checked_out = True

    def check_in (self):
        if not self.__is_checked_out:
            print (f"'{self.title}' is already checked in")
        else: 
            self.__is_checked_out = False

    def get_status (self):
        if self.__is_checked_out == False:
            return f"Available"
        else:
            return f"Checked out"
        
book = Book("1984", "George Orwell")

#check initial status
print (f"{book.get_status()}\n")

#check out book
book.check_out()
print(f"{book.get_status()}\n")

#attempt to check out book
book.check_out()
print(f"{book.get_status()}\n")

#check in book
book.check_in()
print (f"{book.get_status()}\n")

#attempt to check in book
book.check_in()
print (f"{book.get_status()}\n")


