# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Odejda(ABC):
    def __init__(self, V):
        self.V = V

    @property
    def zatrati(self):
        pass

    @abstractmethod
    def abstract(self):
        return 'Шаблон'

    def __add__(self, other):
        return self.zatrati + other.zatrati



class Palto(Odejda):
    @property
    def zatrati(self):
        if self.V != None:
            self.itog = self.V / 6.5 + 0.5
            return self.itog

    def abstract(self):
        return 'Пальто'

class Kostym(Odejda):
    @property
    def zatrati(self):
        if self.V != None:
            self.itog = 2 * self.V + 0.3
            return self.itog

    def abstract(self):
        return 'Костюм'


paltishko = Palto(55)
kostymchik = Kostym(175)
vsego_tkani = paltishko + kostymchik

print(f'Ткани для пальто: {paltishko.zatrati:.1f}')
print(f'Ткани для костюма: {kostymchik.zatrati:.1f}')
print(f'Проверка абстракта: {kostymchik.abstract()}')
print(f'Всего ткани нужно: {vsego_tkani:.1f}')
