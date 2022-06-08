# 1


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([f'{it}' for it in line]) for line in self.matrix)

    def __add__(self, other):
        m = [[int(self.matrix[line][it]) + int(other.matrix[line][it]) for it in range(len(self.matrix[line]))]
                 for line in range(len(self.matrix))]
        return Matrix(m)


a = [[1, 2], [3, 4], [5, 6]]
b = [[7, 8], [9, 10], [11, 12]]

mtr_1 = Matrix(a)
mtr_2 = Matrix(b)
new_m = mtr_1 + mtr_2
print(new_m)