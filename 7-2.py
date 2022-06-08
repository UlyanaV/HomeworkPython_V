# 2

class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def raskhoda_tkani(self):
        return str(f'Общий расход ткани {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

    def coat(self):
        return self.size / 6.5 + 0.5

    def costume(self):
        return self.height * 2 + 0.3


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.res_c = round((self.size / 6.5 + 0.5), 2)

    def __str__(self):
        return f'Площадь на пальто {self.res_c}'


class Costume(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.res_cos = round((self.height * 2 + 0.3), 2)

    def __str__(self):
        return f'Площадь на костюм {self.res_cos}'


clothes_1 = Coat(7, 4)
clothes_2 = Costume(5, 8)
print(clothes_1)
print(clothes_2)
print(clothes_1.raskhoda_tkani)
print(clothes_2.raskhoda_tkani)
