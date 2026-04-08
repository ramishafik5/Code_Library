'''two type of loops condition and counter '''

#condition

'''x = 0
while x < 10:
    print ("x is small")
    x = x + 1'''

'''x = 0
while x < 10:
    print ("x is small")
    x = x - 1'''
'''this will be a infinte loop becuase it 
never meets the condition'''

'''while loop is known as a pretest loop
- test condition is false to sart with
    - wil never execute if condion is false'''

'''counter = 0
total = 0

while counter <= 100:
    total = total + counter
    counter = counter + 1
    print (total)'''

'''while True:
    name = input ("Enter a name: ")
    if name == "Done":
        break
    print (name)
print ("Done")'''

#counter
'''range
One argument: used as ending limit.
Two arguments: starting value and ending limit
Three arguments: the third argument is the step value
'''

'''for x in range(6):
    print (x)'''

'''for i in range (1):
    print(i)'''

'''for i in range (2, 3):
    print (1)'''

'''for i in range (0, 10, 4):
    print(i)'''

'''for i in range (0):
    print(i)'''

'''for i in range (2, 6):
    print (i)'''

'''for i in range (2, 16, 10):
    print (i)'''

'''for i in range (4):
    print(i)'''

'''for i in range (2, 2):
    print (i)'''

'''for i in range (2, 16, 4):
    print (i)'''

'''computer = ["apple", "asus", "bell", "samsung"]
for brands in computer:
    print (brands)'''

'''language = ["python", "c++", "java"]
for x in language:
    if x == "c++":
        break
    print (x)'''

'''language = ["python", "c++", "java"]
for x in language:
    if x == "c++":
        continue
    print (x)'''
#"continue" is like skip while "break" ends at the segmant

'''for i in range (1, 10):
    print (i, end = "")
#end prints the result horizontaly'''

'''for x in range (0, 9, 2):
    print(x, end = "")'''

for i in range  (5):
    for j in range (5):
        print ("*", end = "")
    print ()

for i in range  (5):
    for j in range (5):
        print ("*")
    print ()