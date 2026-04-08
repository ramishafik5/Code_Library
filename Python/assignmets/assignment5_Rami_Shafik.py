#Rami Shafik 100971729

import math #imports math functions
import random #imports random functions 

######################################## Question 1 #########################################

count = 0 # set a begining varibale for count

def increment_count(): #defining the function

    global count #set count as a global variable

    count = count + 1 #set count as previous count plus 1

increment_count() #calls the function
increment_count() #calls the function
increment_count() #calls the function

print (f"the value of the increment count is {count}") #print statment for the result of the count

######################################## Question 2 #########################################

def calculate_squar_root(number): #defining the function with variable
    return math.sqrt(number) #reterns the squar root of the variable

sqrt = int (input ("Enter a positive number")) # input variable form user
result = calculate_squar_root(sqrt) #result of the function from the input variable from user

print (f"the squar root of {sqrt} is {result}") #print statment to show the results

######################################## Question 3 #########################################

def add(a, b): #defining the function with varibale
    return a + b #returns the sum of the variables

def subtract(a, b): #defining the function with variables
    return a - b #returns the difference of the variables

number1 = int (input ("Enter the first number")) #first variable from user
number2 = int (input ("Enter the second number")) #second variable from user

sum = add (number1, number2) #set the variables for the first function
difference = subtract (number1, number2) #set the variables for the second function

print (f"The sum of {number1} and {number2} is {sum} and the difference is {difference}") #print statment to show the results

######################################## Question 4 #########################################

def random_dice(): #defining the function
    return random.randint(1,6) #reterns a number between 1-6

print (f"you rolled a {random_dice()}") #print statment to show the results