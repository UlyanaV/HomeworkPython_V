# 2
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    _length = 0
    _width = 0
    massa = 0
    tolshchina = 0

    def massa_asfalta(self, _length, _width, massa, tolshchina):
        self._length = _length
        self._width = _width
        self.massa = massa
        self.tolshchina = tolshchina
        print((_length * _width * massa * tolshchina)/1000)


a = Road()
a.massa_asfalta(20, 5000, 25, 5)
