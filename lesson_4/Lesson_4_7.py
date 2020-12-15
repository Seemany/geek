# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    z = 1
    v = 1
    while v < n+1:
        z *= v  # Сам факториал
        yield f'Факториал !{v} = {z}'
        v += 1    # Сам счетчик

n = 4

for el in fact(n):
    print(el)

# q = fact(n)
# print(q)
# print(next(q))
# print(next(q))
# # print(next(q))
# # print(next(q))

