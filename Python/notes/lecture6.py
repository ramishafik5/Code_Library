my_set = {1, 2, 3}
print (my_set)

your_set = {1.2, "Hello", (1, 2, 3)}
print (your_set)


a = {}
print (type (a))

a = set()
print (type (a))


a = set()
a.add (2)
print (a)

a.update ([2, 3, 4])
print (a)

a.update ({1, 10, 8, 8})
print (a)

#set's don't accept the same value

a.discard (11)
print (a)

a.pop ()
print (a)

'''a.remove (11)
print (a)  no 11 in set so can't remove'''


a = {1, 2, 3, 4, 5,}
b = {4, 5, 6, 7, 8,}

print (a|b)
print (a.union(b))
print (b.union(a))

print (a & b)
print (a.intersection(b))
print (b.intersection(a))

print (a - b)
print (b - a)
print (a.difference(b))
print (b.difference(a))

print (a ^ b)
print (a.symmetric_difference(b))
print (a.symmetric_difference(b))


my_set = set("apple")
print ("a" in my_set)
print ("p" not in my_set)


for letter in set("apple"):
    print (letter)


small_set = set ("abc")
big_set = set ("abcdef")

print (small_set)
print (big_set)
print (small_set <= big_set)
print (big_set >= small_set)


contacts = {"bill": "353-1234", "rich": "268-1234", "jane": "352-1234"}
print (contacts)

my_dict = {}

my_dict = {1: "apple", 2: "ball"}

my_dict = {"name": "john", 1: [1, 2, 3]}

my_dict = dict ({1: "apple", 2: "ball"})

# douplcated values is ok but not key


my_dictionar = {}

my_dictionar ["bill"] = 25
print (my_dictionar ["bill"])


my_dict = {"name": "Jack", "age": 26}

print (my_dict ["name"])
print (my_dict ["age"])


my_dictionar = {"bill": 3, "rich": 10}
print (my_dictionar ["bill"])

my_dictionar["bill"] = 100
print (my_dictionar ["bill"])


my_dict = {"name": "jack", "age": 26}

my_dict ["age"] = 27

my_dict ["address"] = "downtown"

print (my_dict)


squares = {1:1, 2:4, 3:9, 4:16, 5:25}

print (squares.pop(4))

print (squares)

del squares [5]

print (squares)
print ()

print (squares.popitem())

print (squares)


squares = {1:1, 3:9, 5:25, 7:49, 9:81}

print (1 in squares)
print (2 not in squares)
print (49 in squares)

squares = {1:1, 3:9, 5:25, 7:49, 9:81}
for i in squares:
    print (i)


squares = {1:1, 3:9, 5:25, 7:49, 9:81}
print (len(squares))