# Rami Shafik 100971729

import random #imports the random funtctions

######################################## Prime.py #########################################

def check_prime (): #defining the function 
    num = int (input ("Enter a positive integer ")) #prompts user to enter a positive integer

    while True:
          if num == 1: #if statment to if 1 is imputed
               print (" 1 is niether a prime or conposite number") # print statment if "if" statment is fulflied
               break #break loop if "if" statment is fulfilled

          prime = True #sets the function prime to be true 

          for i in range (2, num): # loop for i to see if number imputed is a prime or conpostion number
               if num % i == 0: #if statment to see if number imputed is dividable by the numbers of i without a remainder 
                    prime = False #set prime to be false to be false if if statment is fulfulled
                    break #end the loop

          print (num) #print the number inputed
          if prime: #if statemt to check if prime remains true
                print ("This is a prime number") #print statment for the if statment 
                break #break loop if "if" statment is fulfilled
          else: #else statment to see if prime is false
                print ("this is a composite number") #print statment for the else statment 
                break #break loop if "else" statment is fulfilled

check_prime () #allows the funtion to run its lines of code and displayes it

######################################## Random.py #########################################

def number_guess (): #defining the function
     number = random.randint (1,100) # allows code to pick a number between the veriables of 1 and 100

     guess = None #assigning guess as a veriable 

     while guess != number: #while loop for when guess does not equal the random number
        guess = int (input ("Guess a number between 1 and 100")) #assigns guess to be the guess of the user 

        if number > guess: #if statment if number is greater than the guessed number
             print (guess) #print the number guessed
             print("Too Low") #print statment letting the number guessed is too low
        elif number < guess: #elif statment if number is less than the guessed number
             print (guess) #print the number guessed
             print ("Too High") #print statment letting the number guessed is too high
        elif number == guess: #elfif statment if number is the guessed number
             print (guess) #print the number guessed
             print ("you guessed it ") #print statment letting the number guessed is correct
             break #break the loop for the while loop if this elif statment is fulfilled 

number_guess () #allows the funtion to run its lines of code and displayes it

######################################## Sum.py #########################################

def even_sum(): #defining the function
    n = int (input ("Enter a postive integer")) # propmt user to input a positive integer

    sum = 0 #set original sum to 0 as nothing has been added yet

    for x in range (2, 1 + n, 2): #loopf for x to check evey even integer including if integer inputed is even
        sum = x + sum #calculates sum by adding sum by the values of x on a loop until all values of x are given

    print (f"the sum of all the even numbers from 1 to {n} is {sum}") #print statment that shows the integer inputed and the sum of even numbers 

even_sum() #allows the funtion to run its lines of code and displayes it

######################################## Die.py #########################################

def dice_role(): #defining the function
     playerA = input ("Enter player A name") #input name for player A
     playerB = input ("enter player B name") #input name for player B

     while True: #infinite loop until break condition is met

        rollA  = input (f"{playerA} type 'roll' to roll the dice") #input "roll" so player A can roll dice
        
        if rollA != "roll": #if statment if player A doesn't type "roll"
             continue #condion of "if" statment which promps player A to retype roll until it inputed
        
        diceA = random.randint (1,6) #random function that allows dice A to be any number form 1-6
        print (f"{playerA} has rolled a {diceA}") #print statment to show the result of the roll
        if diceA == 6: #if statment if dice A is 6 
             print (f"{playerA} is the winner") #print statemnt to let player A know he won 
             break #break the while loop if "if" statment is fulfilled
        
        rollB  = input (f"{playerB} type 'roll' to roll the dice") #input "roll" so player B can roll dice
        
        if rollB != "roll": #if statment if player B doesn't type "roll"
             continue #condion of "if" statment which promps player B to retype roll until it inputed

        diceB = random.randint (1,6) #random function that allows dice B to be any number form 1-6
        print (f"{playerB} has rolled a {diceB}")  #print statment to show the result of the roll
        if diceB == 6: #if statment if dice B is 6 
             print (f"{playerB} is the winner") #print statemnt to let player B know he won
             break #break the while loop if "if" statment is fulfilled
        
dice_role() #allows the funtion to run its lines of code and displayes it