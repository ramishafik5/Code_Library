import os
print (os.getcwd())


file = open ("python.txt", "w")
file.write ("python is fun")
file.close()


file = open ("python.txt", "a")
file.write (" Math is fun")
file.close()


file = open ("python.txt", "r")
final_content = file.read()
print (final_content)
file.close()


try:
    print (x)
except NameError:
    print ("Variable x is not defined")

#print (x)

try:
    x = int (input ("Enter a number: "))
    y = int (input ("Enter another number: "))
    print ("x/y =", x/y)
    print ("x * y =", x*y)
except ZeroDivisionError:
    print ("Invalide y input")
except ValueError:
    print ("Value Error")


x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError as e:
    z = e
    print (z)


try:
    f = open ("list.txt", "r")
    f.read()
except FileNotFoundError:
    print ("Error: can't find file or read data")
else:
    print ("Read content in the file successfully")
    f.close()


