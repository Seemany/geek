# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
test = '11-1-2001'
test1 = '11-18-2001'
test2 = '11-1-2080'
test3 = '40-1-2001'

class Data():
    @classmethod
    def intstrka(cls, strka):
        newstr = []
        strka = strka.split('-')
        for el in strka:
            newstr.append(int(el))
        return newstr

    @staticmethod
    def valitstrka(strka):
        validator = Data.intstrka(strka)
        if 0 < validator[1] <= 12:
            if 1900 < validator[2] <= 2020:
                if 0 < validator[0] <= 31:
                    return f'Дата верна - {strka}'
                else:
                    return f'Число невалидно - {strka}'
            else:
                return f'Год невалидный - {strka}'
        else:
            return f'Месяц невалидный - {strka}'

print(Data.intstrka(test))
print(Data.valitstrka(test1))
print(Data.valitstrka(test))
print(Data.valitstrka(test2))
print(Data.valitstrka(test3))

