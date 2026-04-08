# Rami Shafik 100971729

######################################## Operators.py #########################################

num1 = float(input ("Enter the first number: ")) #ask for number 1 and turn it into a float integer 
num2 = float(input ("Enter the second number: ")) #ask for number 2 and turn it into a float integer 
opp = input("Enter the opporation (add or +, subtract or -, divide or /, multiply or *): ") #ask for either the symbol or teh word of the opporation

if opp == "+" or "add": #if statment for the adding opporation with a "or" to use either the word or symbol
    print ("the result is", num1 + num2) #print the result of the of adding the two numbers after fulfilling the if statment 
elif opp == "-" or "subtract":#if statment for the subtract opporation with a "or" to use either the word or symbol
    print ("the result is", num1 - num2)#print the result of the of subtracting the two numbers after fulfilling the elif statment
elif opp == "/" or "divide":#if statment for the divide opporation with a "or" to use either the word or symbol
    print ("the result is", num1 / num2)#print the result of the of dividing the two numbers after fulfilling the elif statment
elif opp == "*" or "multiply":#if statment for the multiply opporation with a "or" to use either the word or symbol
    print ("the result is", num1 * num2)#print the result of the of multiplying the two numbers after fulfilling the elif statment

######################################## MaxMin.py #########################################

number1 = float(input ("Enter the first number: ")) #ask for number 1 and turn it into a float integer 
number2 = float(input ("Enter the second number: ")) #ask for number 2 and turn it into a float integer 
number3 = float(input ("Enter the third number: ")) #ask for number 3 and turn it into a float integer 

maxNum = max(number1, number2, number3) #determine the max of the 2 numbers inputed
minNum = min(number1, number2, number3)  #determine the min of the 2 numbers inputed

print (f"the greatest number is {maxNum}") #print the greatest number inputed by using a f string
print (f"the smallest number is {minNum}")  #print the greatest number inputed by using a f string

if number1==number2==number3: #if statment to see if the number inputed are the same throughout 
    print ("All three numbers are the same") #print "All three numbers are the same" if "if" statment is fulfilled
else: #else statemnt if "if" statment is not fulfilled
    print ("The numbers are not all the same") #print "The numbers are not all the same" if "else" statment is fulfilled

######################################## PositiveNegative.py #########################################

pNum1 = float(input ("Enter the first number: ")) #ask for number 1 and turn it into a float integer
pNum2 = float(input ("Enter the second number: ")) #ask for number 2 and turn it into a float integer

if pNum1 > 0 and pNum2 > 0: #if statment to see if both numbers are positive with the use of "and"
    print ("both numbers are positve") #print "both numbers are positve" if the if statment is fulfilled
elif pNum1 < 0 or pNum2 < 0: #elif statment to see if one or numbers are negative with the use of "or"
    print ("one or both are negative") #print "one or both are negative" if the elif statment is fulfilled
elif pNum1 == 0 or pNum2 == 0: #elif statment to see if one or both numbers are zero with the use of "or"
    print ("One or both are zero.")  #print "One or both are zero" if the elif statment is fulfilled

######################################## Temperature.py #########################################

temp = float (input ("Enter the temperature in celcius")) #ask user to input the temp in celcius

print (f"Temperature in celcius is {temp} degrees") #print the tempreture given with an f string

if temp >= 30: #if statment to see if the weather is over or is 30 degrees
    print("Hot") #print "Hot" if "if" statment is fulfilled
elif temp >= 15: #elif statment to see if the weather is under 30 degrees and is greater or equal to 15 degrees
    print ("Warm")  #print "Warm" if "elif" statment is fulfilled
elif temp >= 0:#elif statment to see if the weather is under 15 degrees and is greater or equal to 0 degrees
    print ("Cold")  #print "Cold" if "elif" statment is fulfilled
else: #else statment to see if the weather is under 0 degrees
    print ("Freezing cold")  #print "Freezing cold" if "else" statment is fulfilled