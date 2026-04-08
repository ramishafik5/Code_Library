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
        