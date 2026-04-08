# Rami Shafik

class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_numerator = self.x * other.y+ other.x * self.y
        new_denominator = self.y * other.y
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.x * other.y - other.x * self.y
        new_denominator = self.y * other.y
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.x * other.x
        new_denominator = self.y * other.y
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f"{self.x}/{self.y}"

# Test
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2)  
print(f1 - f2)  
print(f1 * f2)  

#wasn't sure if they wanted the numbers to be fractions but did so as the class is called fractions