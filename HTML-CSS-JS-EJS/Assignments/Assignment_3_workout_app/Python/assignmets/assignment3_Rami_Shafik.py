# Rami Shafik 100971729

######################################## Timer.py #########################################

x = 11 #set the variable to 11
while x>0: # loop statment to loop the code utile the condition is met
    x = x-1 #condition in which the code will run until the while condtion is met
    print(x) #print the x variables 
print ("Time's up") #print statment after loop condition is met

######################################## NumberGuess.py #########################################

while True: #infinite loop until break condition is met
    number = int (input ("Enter a Number between 1-50: ")) #user input guess to loop until the the loop is terminated
    if number > 28 : #if statment if the number inputed is > 28
        print ("Too high") #print statment to tell user guess was greater than the number
    elif number < 28: #elif statment if the number inputed is < 28
        print ("Too low") #print statment to tell user guess was less than the number
    elif number == 28: #elif statment to if number inputed is 28
        break #break statment to break the loop
print ("Correct") #print statment to tell user code was correct

######################################## Hunted.py #########################################

attempts = 5 #number of attempts

password = ["ghost", "spirit", "phantom"] #all the passwords user can guess correctly 

while True: #infinite loop until break condition is met
    passwordAttempt = input ("Enter the password to escape the haunted house:") #string variable of the user's password attempt
    
    if passwordAttempt in password: #if statment if the password user inputed was in password
        print ("You escaped the haunted house!") #print statment if "if" statment is met
        break #break statment if "if" statment is met
    else: #else statment if "if" statment is not met
        attempts = attempts - 1 #number of attempt remaining if guessed incorrectly 
        print ("wrong password, you're still trapped") #print statment letting the user know they guessed the wrong password
        if attempts == 0: #if statment inside else statment once attempts is 0
            print ("You're stuck in the haunted house forever") #print statment letting teh user know they have no more attempts 
            break #break statment for the if statment. 

######################################## Solving.py #########################################

'''courses = ["Math", "Science", "History", "Art"]
selected_courses = []

for i in range(7): # 1. should be range(3) to select 3 courses
    course = input("Select a course (Math, Science, History, Art): ) # 2. missing end quotes
    if course in courses:
        if course not iN selected_courses: # 3. n in "iN" is capletalized when it should be all lowecase
            selected_course.append(course) # 4. selected_course should be selected_courses
            print("You have selected:", course)
        else:
        print("You have already selected this course. Please try again.")
    else:
    print("Invalid course selected. Please try again.") # 5. wrong indent on the print statment 

print("You have selected the following courses: selected_courses")# 6. wrong placment of end qoutes and no, to idetify the variable '''

courses = ["Math", "Science", "History", "Art"]
selected_courses = []

for i in range(3):
    course = input("Select a course (Math, Science, History, Art):") 
    if course in courses:
        if course not in selected_courses:
            selected_courses.append(course) 
            print("You have selected:", course)
        else:
            print("You have already selected this course. Please try again.")
    else:
        print("Invalid course selected. Please try again.")

print("You have selected the following courses:", selected_courses)