#Project 3 Group 3.
#November 11th 2024.
#Aidan Waddell 100852734
#Kevin Nguyen 100991505
#Rami Shafik 100971729

#Collaboration Policy
#This is a group assignment. We take academic integrity seriously. Any student found to be involved in plagiarism or cheating will be penalized in accordance to the Ontario Tech Calendar Section 5.15.
#The official policy of the instructor is that it is acceptable to discuss general strategies with your fellow students, but when it comes to actually writing code, your team should do it entirely alone. Do not share your code with anyone.
#Any team who turns in work copied (in whole or in part) from another team will result in both (or all) students being investigated for a violation of academic integrity, which will result in failure of the assignment, a permanent record of the incident on your academic record, and possible further consequences.
#To assert that you have not given or received, or used unauthorized assistance, write the following pledge in the comment textbox when you submit your files through Canvas system.
#"I Aidan Waddell, Kevin Nguyen, and Rami Shafik have not given, received, or used any unauthorized assistance."

#The purpose of this program is to develop a student ledger that also displays the details about the student.
#the program should allow the user to enter a non-case sensitive username of "Admin" and the case-sensitive
#password "password". Upon logging in the user should be directed to an interface that gives them the
#option to add new student information, access a database, search up the details of a student within the
#database, or exit the program altogether. Upon entering an empty database, the user will be told that
#no queries exist and that they must add a student within the database to store it in that part of the interface.
#Once established within the database, the user will be given the option to search up individual student
#details within the search option of the home interface after the student details have been provided to the
#student database.

import random #Importing the random module.
from prettytable import PrettyTable #Importing the PTable module.

data = [] #Create the global variable of data outside the functions as it represents what is contained within our database.


def admin(): #Define the admin function. This is our main function.
        print("Admin Login Page") #This will print our admin login page header.
        username = input("Enter username: ") #This will create our username input.
        password = input("Enter password: ") #This will create our password input.

        if username == "Admin" and password == "password": #Create conjunction for username and password. NOTE: Password must be lowercase.
            menu () #If both are true, then we run the menu function.
        else: #If both are not true however,
            print("Invalid Username or Password, please try again.") #We print an invalid statement.
            admin ()#Then we rerun the admin function.

def menu (): #Define the menu function to show all the options in our Home Interface.
    while True: #Create the infinite loop.
        print("\nStudent Ledger") #Create the student ledger header.
        print ("[1] Add a new student") #Option to add a new student.
        print ("[2] Display student database") #Option to show the database.
        print ("[3] Search student details") #Option to search the student details.
        print ("[4] Exit the system") #Option to exit the system.
        print("Enter [1], [2], [3] or [4]") #Choices given.

        interface = input("") #Input to insert interface options.

        if interface == "1": #If it is equal to 1, run the menu function.
            new () #Run the menu function.
        elif interface == "2": #If it is equal to 2, run the database function.
            database () #Run the database function.
        elif interface == "3": #If it is equal to 3, run the search function.
            search () #Run the search function.
        elif interface == "4": #If it is equal to 4, exit the system.
            print ("Exiting system.") #Print that we are exiting the system.
            admin() #Run the admin function and bring us back to the login.
        else: #Otherwise.
            print ("Invalid input.") #If the input is not 1, 2, 3, or 4, then continue until the user gives the right input.
            continue #Continue the while loop.

def new(): #Define the new function.
    student_number = random.randint(2000, 3000) #Set the variable of student number to any random number between 2000, 3000. Each time the function is run, a completely new random number is produced.
    print("Please enter student details below: ") #Header for the student details.
    first_name = (input("First Name: ")) #Student first name input.
    middle_name = (input("Middle name: ")) #Student middle name input.
    last_name = (input("Last Name: ")) #Student last name input.
    DOB = (input("Enter Date of Birth: ")) #Date of birth input.
    gender = (input("Enter Gender: ")) #Gender input.
    department = (input("Enter Department: ")) #Department input.
    email = input("Enter Email: ") #Email input.
    phone_number = input("Enter Phone Number: ") #Phone number input.
    emergency = input("Enter Emergency Contact Details: ") #Emergency input.
    courses = input("Courses Opted: ") #Courses input.
    schedule = input("Student Detailed Schedule: ") #Student schedule input.
    fees = input("Information about fees: ") #Fees input.
    awards = input("Awards and financial aid (if None enter 'None'): ") #Awards input.
    grades = input("Final grades: ") #Final grades input.

    student = {
        "Student Number": student_number, #Key and value for the student number.
        "First Name": first_name, #Key and value for first name of student.
        "Middle Name": middle_name, #Key and value for middle name of student.
        "Last Name": last_name, #Key and value for last name of student.
        "Date Of Birth": DOB, #Key and value for date of birth of student.
        "Gender": gender, #Key and value for gender of student.
        "Department": department, #Key and value for department of student.
        "Email": email, #Key and value for email of student.
        "Phone Number": phone_number, #Key and value for phone number of student.
        "Emergency Contact": emergency, #Key and value for emergency contact of student.
        "Courses Opted": courses, #Key and value for courses opted by the student.
        "Student Detailed Schedule": schedule, #Key and value for the students schedule.
        "Fees": fees, #Key and value for the fees of the student.
        "Awards": awards, #Key and value for the awards of the student.
        "Grades": grades, #Key and value for the grades of the student.
    }

    while True: #Create an infinite loop.
        print("Would you like to save this student Data. Please type Yes or No.") #Print option to save students data.
        save_data = input("").strip().lower() #Create input for the saved data.
        if save_data == "yes": #If the input is yes.
            data.append(student) #Then append the dictionary of student into the data table. Now it will appear in the database.
            print("Do you wish to enter another student? Please type Yes or No.")  # Print option to enter another students details.
            another = input("").strip().lower()  # Create the input for another student.
            if another == "yes":  # If the input is yes.
                new()  # Rerun the new function to add a new student.
            elif another == "no":  # However, if the input is no.
                table = PrettyTable()  #Create a new PrettyTable object.
                table.field_names = ["Student Number", "First Name", "Middle Name", "Last Name", #Create the list of students to post when user inputs no.
                                     "Date Of Birth", "Gender", "Department",
                                     "Email", "Phone Number", "Emergency Contact",
                                     "Courses Opted", "Student Detailed Schedule", "Fees", "Awards", "Grades"]

                table.hrules = 1 #Create the horizontal line rules for the PTable.

                for student in data:  #Take the necessary dictionary in the data object and iterare through it.
                    table.add_row([student["Student Number"], student["First Name"], student["Middle Name"], student["Last Name"], #Go through each key with each value.
                         student["Date Of Birth"], student["Gender"], student["Department"],
                         student["Email"], student["Phone Number"], student["Emergency Contact"],
                         student["Courses Opted"], student["Student Detailed Schedule"], student["Fees"],
                         student["Awards"], student["Grades"]])
                print(table) #We print the table to show that the information of the student is in the database.
                menu()
            else:
                print("Invalid input, must insert Yes or No.") #User must only insert yes or no.
                continue #Continue the while loop until they insert yes or no.
        elif save_data == "no": #Otherwise if they input no.
            student.clear() #If the answer is no, clear the information from the student dictionary.
            menu() #Return to the menu using the menu function.
        else: #If neither input is given.
            print("Invalid input, must insert Yes or No.") #Then tell the user to put in the proper input.
            continue #Continue the loop until the user gives the right input.

def database (): #Define the database function.
    if not data: #The function checks if the value of data does not exist.
        while True: #If it is true that it does not exist, then an infinite loop is created.
            print ("No data available please add a student\n Please enter the following: \n [1] Main Menu \n [2] Exit.") #Tell the user no data is available and give them the options to return to the main menu, or exit the system.
            return_menu = input("") #Create the input of return_menu to return back to the main menu.
            if return_menu == "1": #If the user inputs 1, return to the main menu.
                menu() #Rerun the menu function.
            elif return_menu == "2": #If the user inputs 2, return to the login by rerunning the admin function.
                admin() #Rerun the admin function.
            else: #If neither of the above are true.
                print("Invalid input.") #Show that they put in an invalid input.
                continue #Continue the function until they put in a valid input.

    else: #However, if the data list does have values inside of them. Then we can do the following;

        table = PrettyTable() #We can create a new PTable object.
        table.field_names = ["Student Number", "First Name", "Middle Name", "Last Name", #We can create the given field names for each category.
                             "Date Of Birth", "Gender", "Department",
                             "Email", "Phone Number", "Emergency Contact",
                             "Courses Opted", "Student Detailed Schedule", "Fees", "Awards", "Grades"]
        table.hrules = 1 #Create the rules for the horizontal lines of the PTable.

        for student in data: #Then we take out the dictionary of student from the data list.
            table.add_row([student["Student Number"], student["First Name"], student["Middle Name"], student["Last Name"], #We then add individual rows for each category.
                          student["Date Of Birth"], student["Gender"], student["Department"],
                          student["Email"], student["Phone Number"], student["Emergency Contact"],
                          student["Courses Opted"], student["Student Detailed Schedule"], student["Fees"], student["Awards"],student["Grades"]])

        print(table) #We print the table to show that the information of the student is in the database.



def search (): #Define the search function for a student.
    student_number = int(input("Please input student number: ")) #Create the local variable of student_number to input the number of the student.

    table = PrettyTable() #Create a PrettyTable object to get the necessary student details.
    table.field_names = ["Student Number", "First Name", "Middle Name", "Last Name", #These are the student details.
                        "Date Of Birth", "Gender", "Department",
                        "Email", "Phone Number", "Emergency Contact",
                        "Courses Opted", "Student Detailed Schedule", "Fees", "Awards", "Grades"]

    found = False #Create variable called found to find the student, and set it to false.

    for student in data: #Iterate through the values of student in the data list to look for our given student.
        if student["Student Number"] == student_number: #Condition for whether or not the student number we are looking for is in the list of values.
            table.add_row([student["Student Number"], student["First Name"], student["Middle Name"], student["Last Name"], #If it is, show all of their information in the form of a pretty table.
                          student["Date Of Birth"], student["Gender"], student["Department"],
                          student["Email"], student["Phone Number"], student["Emergency Contact"],
                          student["Courses Opted"], student["Student Detailed Schedule"], student["Fees"], student["Awards"], student["Grades"]])

            found = True #If the above statement is true, then the variable of found is set to true.

        if found: #If found is true then we create the conditions below to print the table of the student.
            print(table) #Print the table.
            print("Please enter the following options below:\n[1] Main Menu\n[2] Exit \n[3] Continue Searching for Students") #Show the interface options.
            search_interface = input("") #Create the search_interface variable.
            if search_interface == "1": #If they insert 1.
                menu() #Return to the menu using the menu function.
            elif search_interface == "2": #If they insert 2.
                admin() #Return to the main interface using the admin function.
            elif search_interface == "3": #If they insert 3.
                search() #Continue searching for the student.
        else: #Otherwise.
            print("Student not found in database.") #State that the student is not in the database.
            search() #Return the user to the search function.



admin() #Run the admin function to run the program.
