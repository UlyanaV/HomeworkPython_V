# 4

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, napravleniye):
        return f'{self.name}' + ' повернула ' + f'{napravleniye}'

    def show_speed(self):
        return f'{self.speed} текущая скорость автомобиля {self.name}'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'{self.speed} текущая скорость автомобиля {self.name}')
        if self.speed > 60:
            return f'Скорость {self.name} выше 60'


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'{self.speed} текущая скорость автомобиля {self.name}')
        if self.speed > 40:
            return f'Скорость {self.name} выше 40'


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = SportCar(100, 'White', 'Audi')
lada = TownCar(110, 'Green', 'Lada')
kamaz = WorkCar(70, 'Black', 'Камаз')
ford = PoliceCar(90, 'Blue',  'Ford', True)
print(audi.go())
print(lada.turn('лево'))
print(kamaz.turn('право'))
print(ford.stop())
print(audi.show_speed())
print(lada.show_speed())
print(kamaz.show_speed())
