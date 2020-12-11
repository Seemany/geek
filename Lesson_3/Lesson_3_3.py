# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    s = a,b,c
    z = sorted(s)
    maximum = z[1]+z[2]
    return maximum

print(my_func(3,2,1))

