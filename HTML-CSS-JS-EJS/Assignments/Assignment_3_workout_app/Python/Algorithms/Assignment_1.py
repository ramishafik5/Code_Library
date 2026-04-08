class ThreeColorStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity

        self.red_top = -1
        self.green_top = capacity // 3 - 1
        self.blue_top = capacity

    def push_red(self, item):
        if self.red_top + 1 < self.green_top:
            self.red_top += 1
            self.array[self.red_top] = item
        else:
            raise Exception("Red Stack Overflow")

    def push_green(self, item):
        if self.green_top + 1 < self.blue_top:
            self.green_top += 1
            self.array[self.green_top] = item
        else:
            raise Exception("Green Stack Overflow")

    def push_blue(self, item):
        if self.blue_top - 1 > self.green_top:
            self.blue_top -= 1
            self.array[self.blue_top] = item
        else:
            raise Exception("Blue Stack Overflow")

    def pop_red(self):
        if self.red_top >= 0:
            item = self.array[self.red_top]
            self.red_top -= 1
            return item
        else:
            raise Exception("Red Stack Underflow")

    def pop_green(self):
        if self.green_top >= self.capacity // 3:
            item = self.array[self.green_top]
            self.green_top -= 1
            return item
        else:
            raise Exception("Green Stack Underflow")

    def pop_blue(self):
        if self.blue_top < self.capacity:
            item = self.array[self.blue_top]
            self.blue_top += 1
            return item
        else:
            raise Exception("Blue Stack Underflow")

    def is_empty_red(self):
        return self.red_top == -1

    def is_empty_green(self):
        return self.green_top == self.capacity // 3 - 1

    def is_empty_blue(self):
        return self.blue_top == self.capacity

    def print_stacks(self):
        red_stack = self.array[: self.red_top + 1]
        green_stack = self.array[self.capacity//3 : self.green_top + 1]
        blue_stack = self.array[self.blue_top :]

        print(f"Red Stack: {red_stack}")
        print(f"Green Stack: {green_stack}")
        print(f"Blue Stack: {blue_stack}")