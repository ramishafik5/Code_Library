

def evenOdd(n) :
   if n % 2 == 0 :
      return "even"
   return "odd"
evenOdd()

num = int(input("Enter an integer: "))
print("The integer is", evenOdd(num))