data =[]

def admin():
        print("Admin Login Page")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "Admin" and password == "password":
            menu ()
        else:
            print("Invalid Username or Password, please try again.")
            admin ()

def menu ():
    while True:
        print("\nStudent Ledger")
        print ("[1] Add a new student")
        print ("[2] Display student database")
        print ("[3] Search student details")
        print ("[4] Exit the system")

        interface = input ("Enter 1, 2, 3 or 4")

        if interface == "1":
            new ()
        elif interface == "2":
            database ()
        elif interface == "3":
            search ()
        elif interface == "4":
            print ("exiting system")
            break
        else:
            print ("invalid input")
            continue
        
def database ():

    if not data:
        print ("No data available please add a student")
    else:
        #make a chart of the students information
        dictionary = {}

        for i in data:
            if i in dictionary:
                dictionary[i]

        print("Keyword_name".ljust(20) + "Count")
    print("-" * 25)
    for keyword, count in sorted_dictionary.items():
        print(keyword.ljust(20), count)


    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    
    print("Keyword_name".ljust(20) + "Count")
    print("-" * 25)
    for keyword, count in sorted_dictionary.items():
        print(keyword.ljust(20), count)
    print ("[1] Main menu")

    while True:
        return_menu = input ("Enter 1 to return to menu")
        if return_menu == "1":
            menu ()
        else:
            print ("invalid input. Try again")
            continue
    

def new ():
    print("Please enter student details below: ")
    first_name = (input("First Name: "))
    last_name = (input("Last Name: "))
    DOB = (input("Enter Date of Birth: "))
    gender = (input("Enter Gender: "))
    department = (input("Enter Department: "))
    email = input("Enter Email: ")
    number = input("Enter Phone Number: ")
    emergency = input("Enter Emergency Contact Details: ")
    courses = input("Courses Opted: ")
    fees = input("Information about fees: ")
    awards = input("Awards and financial aid (if None enter 'None'): ")
    grades = input("Final grades: ")

    student = {
        "First Name": first_name, 
        "Midle Name"
        "Last Name": last_name,
        "Date Of Birth": DOB,
        "Gender": gender,
        "Department": department,
        "Email": email,
        "Phone Number": number,
        "Emergency Contact": emergency, 
        "Corses Opted": courses, 
        "Fees": fees, 
        "Awards": awards,
        "Grades": grades
    }
    
    save_data = input ("Would you like to save this student Data. y/m").strip().lower()
    if save_data == "y":
        data.append (student)
    else:
        print ("student data will not be saved")
        another = input ("do you wish to enter onther  student y/n").strip().lower()
        if another == "y":
            new ()
        else:
            menu ()

def search ():
    1

admin ()
