def say_hell(name):
    print (f"hello {name} !")
    print ("what a lovely day")


def f(x):
    return x*x
#"return" returns the value


def main():
    value = 5
    show_double(value)


def show_double (number):
    result = number * 2
    print (result)


def sum(num1, num2):
    result = num1 + num2
    print(result)


def hello(name):
    yourName = (f"hello {name}")
    print (yourName)

hello ("sara")

'''
def area ():
    length = float(input ("length"))
    width = float(input ("width"))
    a = length * width
    return (a)

a = area ()

print ("the are is ", a)'''


def smallest (x, y, z):
   return min(x, y, z)

test1 = smallest (20, 10, 30)
test2 = smallest (0, -1, 1)
test3 = smallest (3.5, 2.5, 6.5)

print (test1, test2, test3)


def vcub (side):
    return (side ** 3)

print (vcub(2))


def allTheSame (x, y, z):
    if x == y == z:
        return True
    else:
        return False

allTheSame (2,3,2)


def NotAllTheSame (a, b, c):
    if a != b != c:
        return True
    else:
        return False
    
NotAllTheSame (2,3,2)

def sorted (d,e,f):
    if d <= e <= f:
        return True
    else:
        return False
    
sorted (7,8,9)


def calualte (m, n):
    add = m + n
    sub = m - n
    mul = m * n
    return add, sub, mul

calualte (float(input()), float(input()))