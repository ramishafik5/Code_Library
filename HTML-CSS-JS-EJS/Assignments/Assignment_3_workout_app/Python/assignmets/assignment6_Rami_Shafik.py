#Rami Shafik 100971729

import math

######################################## Lists.py #########################################

def CheckEvenOdd(mylist):
    even = []
    odd = []

    for i in mylist:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

def CalculateAverage(mylist):
    even, odd = CheckEvenOdd(mylist)
    
    if even:
        even_sum = 0
        for i in even:
            even_sum += i
        avgeven = even_sum / len(even)
    else:
        avgeven = None
        
    if odd:
        odd_sum = 0
        for i in odd:
            odd_sum += i
        avgodd = odd_sum / len(odd)
    else:
        avgodd = None
    
    return avgeven, avgodd

def PrintResults(avgeven, avgodd):
    if avgeven != 0:
        print(f"Average of even numbers: {avgeven}")
    else:
        print("No even numbers were entered.")
        
    if avgodd != 0:
        print(f"Average of odd numbers: {avgodd}")
    else:
        print("No odd numbers were entered.")

def CalculatePow(mylist):

    pow_list = [pow(i, index) for index, i in enumerate(mylist)]

    return pow_list

def final():
    while True:  
        mylist = []
       
        while True:
                num = int(input("Enter a number (-1 to stop): "))
                if num == -1:
                    break
                mylist.append(num)

        avgeven, avgodd = CalculateAverage(mylist)
        PrintResults(avgeven, avgodd)
        
        pow_list = CalculatePow(mylist)
        print(f"Power calculation for each index {pow_list}")

        while True:
            repeat = input("Do you want to repeat? (yes/no): ").strip().lower()
            if repeat != "yes" and repeat != "no":
                print("Please type in yes or no if you want to repeat")
                continue
            else:
                break

        if repeat != 'yes':
            break
        
final()