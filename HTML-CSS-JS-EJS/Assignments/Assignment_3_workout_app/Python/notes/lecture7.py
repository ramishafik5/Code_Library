var = "Happy Halloween!"
for char in var:
    print (char, end = "*")

lst= []
var = "Happy Halloween!"
for char in var:
    lst.append(char)

print (lst)


def function1 (a, b, c):
    print (a, b, c)

list1 = [1, 2, 3]
function1 (*list1)

def add_number (*args):
    sum_number = 0

    for i in range (0, len(args)):
        sum_number += args[i]

    return sum_number

print (add_number(1, 9, 8, 7))
print (add_number(12, 23))


var = "Happy Halloween!"
print (*var)

lsit = [1,4, 5, 8]
print (*lsit)

tup = 1, 4, 5, 8
print (*tup)

str1 = "Hello"
str2 = "world"

print (str1 + ' '+ str2)


str1 = "Hello"
print (str1[0])

#str1[0] = 1


sentence = "python is fun"

first5letter = sentence [0:5]
print (first5letter)

letter3thru4 = sentence [1:4]
print (letter3thru4)

last3letters = sentence[-3:]
print (last3letters)

first3letter = sentence [:3]
print (first3letter)

threelettersbeforelast = sentence [-4:-1]
print (threelettersbeforelast)

copyofstring = sentence [:]
print (copyofstring)


sentence = "Hello World!"
counter = 0

for c in sentence:
    if c == "e":
        counter +=1
    else:
        "Not found"
#print ("there is(are)", counter, "\e", "in this sentence")

password = ("enter password")

def valid_password (password):
    for ch in password:
        if ch.isupper ():
            has_uppercae = True
        if ch.islowwer ():
            has_lower_case = True
        if ch.isspecial ():
            has_special = True


sentence = "Hello world 123!"

print (sentence.isalpha())


sentence = "Hello world 123!"

print (sentence.lower())
print (sentence.upper())
print (sentence.lstrip())
print (sentence.rstrip())
print (sentence.strip())

sentence = "Hello world 123!"

print (sentence.lstrip("H"))
print (sentence.rstrip("o"))
print (sentence.strip("h"))


sentence = "Hello World"

print (sentence.startswith("Hel"))
print (sentence.endswith ("LLO"))
print (sentence.endswith ("llo"))


str1 = "I love programing"
str2 = "prog"

print (str1.find(str2))
print (str1.find(str2, 12))
print (str1.find(str2, 3, 9))
print (str1.find(str2, 3, 12))


str1 = "I love programing"

print (str1.replace ("love", "hate"))


def are_anagrams (word1, word2):
    return sorted(word1) == sorted (word2)

print (are_anagrams ("iceman", "cinema"))
print (are_anagrams ("hello", "world"))

def main ():
    for count in range (1,10):
        print ("z" * count)


    for count in range (8, 0, -1):
        print ("z" * count)
main ()


text = "10.452.909"
print (text.split ("."))
print (text.split (","))

print ("a, b, c".split(","))


date = "11/26/2019"

date_list = date.split("/")
print (date_list)

print ("month:", date_list [0])
print ("month:", date_list [1])
print ("month:", date_list [2])


list1 = list ("1234")
str1 = " "
print (str1.join(list1))

tup1 = tuple ("1234")
print (str1.join(tup1))

str2 = "ABCD"
str3 = "$#@%"

print (str2.join(str3))
print (str3.join(str2))