# 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))


a = Position('Иван', 'Иванов', 'manager', 100000, 25632)
a.get_full_name()
a.get_total_income()
