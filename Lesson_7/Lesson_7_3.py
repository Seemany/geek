# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
#     Сложение.
# Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#     Вычитание.
# Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
#     Умножение.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#     Деление.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Kletka:
    def __init__(self, klet):
        self.klet = int(klet)

    def __add__(self, other):
        return f'Сложение клеток равно клеток: {self.klet + other.klet}'

    def __sub__(self, other):
        vichet = self.klet - other.klet
        if vichet > 0:
            return f'Вычитание клеток: {vichet}'
        else:
            return f'Клетки больше нет'

    def __mul__(self, other):
        return f'Умножение равно: {self.klet * other.klet}'

    def __truediv__(self, other):
        return f'Деление равно: {self.klet // other.klet}'

    def make_order(self, echeyka):
        itog = ''
        kolvostrok = int(self.klet / echeyka)
        for i in range(kolvostrok):
            stroka = echeyka * '*' + '\n'
            itog += stroka
        if self.klet % echeyka == 0:
            return itog
        else:
            itog = itog + (self.klet % echeyka) * '*'
            return itog


pervaya = Kletka(19)
vtoraya = Kletka(5)
print(pervaya + vtoraya)
print(pervaya - vtoraya)
print(pervaya * vtoraya)
print(pervaya / vtoraya)
print(pervaya.make_order(5))