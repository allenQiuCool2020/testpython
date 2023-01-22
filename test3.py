class Operator:
    def __init__(self, name):
        self.name = name

    def plus(self, x, y):
        sum = x + y
        print(sum)

a = Operator("plus")
print(a.name)
a.plus(1, 0)