# 3

class Cell:

    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return self.cell - other.cell

    def __truediv__(self, other):
        return round(self.cell / other.cell)

    def __mul__(self, other):
        return self.cell * other.cell

    def make_order(self, row):
        res = ''
        for i in range(int(self.cell / row)):
            res += f'{"*" * row} \n'
        res += f'{"*" * (self.cell % row)}'
        return res


a = Cell(10)
b = Cell(5)
print(a.make_order(3))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b.make_order(2))
