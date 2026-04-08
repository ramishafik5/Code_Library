'''As a member of the Ontario Tech University community, I share our community’s
commitment to the highest standards of academic integrity and excellence in all
dimensions of our work.

I, therefore, promise that I will not lie, cheat, or use any unauthorized aids or assistance to
complete any of my essays, assignments, and exams. I further promise that I will not offer
any unauthorized assistance to any of my fellow students, and I promise that I will not ask
any of my fellow students for unauthorized assistance. I promise that the work I submit is
my own and that where I have drawn on the work of others, I have included proper
attribution for my sources.

Rami Shafik 100971729
'''

######################################## Anagram Checker #########################################

def is_anagram(string1, string2):
    print ("First string", string1)
    print ("Secodn string", string2)

    words1 = str (len(string1.replace (" ", "")))
    words2 = str (len(string2.replace (" ", "")))

    return sorted(words1) == sorted(words2)

is_anagram (str(input("enter a string")), str(input("Enter another string")))

######################################## [Treasure Hunt Navigator] #########################################

import math

import math

def hunt ():
    try :
        left = int(input("enter setps left"))
        right = int(input("enter setps left"))
        up = int(input("enter setps left"))
        down= int(input("enter setps left"))

    
        d = math.sqrt (((right - left)**2)+((up - down)**2))

        return ("he travild a distance of the hunter", d)
    
    except ValueError or ZeroDivisionError:
        print ("Please enter a number only")

hunt ()

######################################## Grocery Store Manager]#########################################

def initialize_item(name, price_per_kg, weight):

    item = {
        'name': name,
        'price': price_per_kg,
        'weight': weight
    }

    return item

initialize_item  (name, price_per_kg, weight)

def calculate_discount(cost):