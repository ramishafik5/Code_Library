import math
import random


def average(x, y, z):
    return (x + y + z)/3

average(2,4,6)


def area_circle(raduis):
    return math.pi * pow (raduis, 2)

area_circle(int (input("Enter the radius")))


'''def word_count(word):
    return (math.split [word])

word_count(input ("write a sentence"))'''


number = random.randrange (10)
number1 = random.randrange (5,10)
number2 = random.randrange (0, 101, 10)

print (number, number1, number2)

print (random.randint (1,100))

print (random.randint (1,2))

def main():
    for count in range(5):
        number = random.randint (1,10)
        print(number)

main()


def main2():
    for count in range(5):
        number = random.randrange (1,10,4)
        print(number)

main2()


number = random.random()
print (number)

number = random.uniform (1, 10)
print(number)

def coin_flip():

    flip = 10

    while True:
        coin = random.randint (1,2)

        if coin == 1:
            print ("Heads")
            flip = flip - 1
        else:
            print ("Tails")
            flip = flip - 1

        if flip == 0:
            break
        
coin_flip()


def isLeapYear (year):

    if year >=1000 and year % 400 == 0:
        print ("This is a leap year")
    elif year < 1000 and year % 4 == 0:
        print ("this is a leap year")
    else:
        print ("this is not a leap yeat")

isLeapYear(40)


def dice_role():
     playerA = input ("Enter player A name")
     playerB = input ("enter player B name")

     while True:

        rollA  = input (f"{playerA} type 'roll' to roll the dice")
        
        if rollA != "roll":
             continue
        
        diceA = random.randint (1,6)
        print (f"{playerA} has rolled a {diceA}")
        if diceA == 6:
             print (f"{playerA} is the winner")
             break 
        
        rollB  = input (f"{playerB} type 'roll' to roll the dice")
        
        if rollB != "roll": 
             continue

        diceB = random.randint (1,6) 
        print (f"{playerB} has rolled a {diceB}")  
        if diceB == 6:  
             print (f"{playerB} is the winner")
             break
        
dice_role()