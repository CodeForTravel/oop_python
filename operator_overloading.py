class OperatorOverloading:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return OperatorOverloading(x, y)


p1 = OperatorOverloading(1, 2)
p2 = OperatorOverloading(2, 3)


print(p1+p2)
