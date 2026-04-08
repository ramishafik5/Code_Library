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

######################################## Question 7 #########################################

intial_balance = float (input ("Enter your intaila balcne"))

while True:
    prompt_user = int (input ("Enter 1 if you want to deposit or 2 if you want to withdraw"))

    if prompt_user  != 1 and  prompt_user != 2:
            print ("please 1 if you want to deposit or 2 if you want to withdraw")
            continue
    
    def deposit ():
        deposit_amount = float (input ("Enter deposit amount"))
        depoist_balance = round (deposit_amount + intial_balance, 2)
        print (depoist_balance)

    def withdraw ():
        while True:
            withdraw_amount = float (input ("Enter withdraw amount amount"))
            if withdraw_amount > intial_balance:
                print ("Insufficient funds")
                continue
            else:
                withdraw_balance = intial_balance - withdraw_amount
                print (withdraw_balance)
                break

    if prompt_user == 1:
        deposit ()
        break
    elif prompt_user == 2:
        withdraw ()
        break
        
######################################## Question 3 #########################################

age = 0
ages = 5

def age_inp ():
    global age
    global ages

    while True:
        age1 = int (input ("Enter an age in numbers."))
        if age1 >= 65:
            print ("Senior")
        elif age1 >= 20:
            print("Adult")
        elif age1 >= 13:
            print ("Teen")
        else:
            print ("Child")
        
        age += age1
        ages = ages - 1 

        if ages == 0:
            break
age_inp()

def calc_average():
    return age / 5

calc_average ()

######################################## Question 4 #########################################

apple = float (input ("Enter the amount of kilograms of apples sold"))
banana = float (input ("Enter the amount of kilograms of bananas sold"))
cherries = float (input ("Enter the amount of kilograms of cherries sold"))

total_kg = apple + banana + cherries

apple_rev = apple * 3
banana_rev = banana * 2
cherries_rev = cherries * 5

rev = round (apple_rev + banana_rev + cherries_rev, 2)

print (f"You sold a total of {total_kg} kg of furit and genatated ${rev}")

######################################## Question 5 #########################################

def Fbalance (p, r, t):
    print ("Your future value is $", round (p * (1 + r/100) ** t, 2))

Fbalance(float (input("Enter your intail amount")), float (input("Enter your interst rate %")), float (input("Enter numebr of months")))