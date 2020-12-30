# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.



perviy = [[31, 22], [37, 43], [51, 86]]
perviy1 = [[1, 1], [1, 1], [1, 1]]
vtoroy = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
vtoroy1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
tretiy = [[3, 5, 8, 3], [8, 3, 7, 1]]


class Matrix():
    def __init__(self, spisokspiskov):
        self.spisokspiskov = spisokspiskov
        self.stroka = ''
        for elem in self.spisokspiskov:
            for el in elem:
                self.stroka = self.stroka + '\t' + str(el)
            self.stroka = self.stroka + '\n'

    def __str__(self):
        self.strka = str(self.stroka)
        return self.strka

    def __add__(self, other):
        self.summatrix = []
        self.itogchislo = []
        for elem in range(len(self.spisokspiskov)):
            for el in range(len(self.spisokspiskov[0])):
                self.chislo = self.spisokspiskov[elem][el] + other.spisokspiskov[elem][el]
                self.itogchislo.append(str(self.chislo))
                if len(self.spisokspiskov[0]) == len(self.itogchislo):
                    self.summatrix.append(self.itogchislo)
                    self.itogchislo = []
        return Matrix(self.summatrix)


mat1 = Matrix(perviy)
mat2 = Matrix(perviy1)
print(mat1)
print(mat1+mat2)





