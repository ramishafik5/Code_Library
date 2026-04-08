# Rami Shafik 100971729


######################################## Table.py #########################################

a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5

b1 = 2
b2 = 3
b3 = 4
b4 = 5
b5 = 6

ab1 = str(a1 ** b1)
ab2 = str(a2 ** b2)
ab3 = str(a3 ** b3)
ab4 = str(a4 ** b4)
ab5 = str(a5 ** b5)

print( a1, b1, ab1 )
print( a2, b2, ab2 )
print( a3, b3, ab3 )
print( a4, b4, ab4 )
print( a5, b5, ab5 )

######################################## SumOfDigits.py #########################################

number = eval (input("enter a number between 0-1000"))

print (number)

number1 = number//100
number2 = number//10
number3 = number2%10
number4 = number%10

sum= int (number1 + number3 + number4)

print (" the sum of the diget is", sum )

######################################## Arithemetic.py #########################################

print ("7 + 4 =", 7+4) #I simply added 4 to 7 to get the end result of 11
print ("15 - 9 =", 15-9) #I subtracted 9  from 15 to get 6 as my result 
print ("16 // 5 =", 16//5) #I floor devieded 16 form 5 to get 3 as my answer instead of 3.2
print ("8 * 2 =", 8*2) #I multiplied 8 by 2 to get my result of 16
print ("16 / 5 =", 16/5) #I devieded 16 form 5 to get ,y result of 3.2
print ("5 ** 4 =", 5**4) #I transformed the 5 by powering it to the power 4 to get 625
print ("20 % 7 =", 20%7) #I transformed the 20 to 6 by finding the remainder by using the modulus % by 7

######################################## TVshows.py #########################################

tv = input("enter a tv show")
season = eval(input ("enter how many seasons the show has"))
episodes = eval(input("enter how many episodes per season"))
total = season * episodes
print ("the show", tv, "has a total of", total, "episodes" )

######################################## Payroll.py #########################################

name = input("Enter your name")
hours = eval(input("Enter your hours worked"))
rate = eval(input("Enter your hourly rate"))
federal = eval(input("Enter federal tax rate"))
state = eval(input("Enter state tax rate"))

gross = hours * rate

fdeductions = round (gross * federal)
fpercent = round ((100 * federal), 2)

sdeductions = round (gross * state)
spercent = round ((100 * state), 2)

tdeducutions  = round (sdeductions + fdeductions)

net = (gross - tdeducutions)

print ("Emplyee name:", name)
print ("Hours worked:", hours)
print ("Pay rate:$", rate)
print ("Gross pay:$", gross)
print ("  Federal withholding (",fpercent, "):",fdeductions )
print ("  State withholding (",spercent, "):",sdeductions)
print ("  Total deduction:", tdeducutions)
print ("Net pay: ", net)