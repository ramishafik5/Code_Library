# Question 7: Counting Instances of a Class


class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 1  

a = Counter()
b = Counter()
c = Counter()

print(Counter.count)

