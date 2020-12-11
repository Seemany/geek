# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

spisok = [1,1.2,'vtoroy',True]

for n in spisok:
    if type(n) == object:
        print(f'{n} это тип int')
    elif type(n) == float:
        print(f'{n} это тип float')
    elif type(n) == str:
        print(f'{n} это тип str')
    elif type(n) == bool:
        print(f'{n} это тип bool')
    else:
        print(f'{n}, Не такой тип, он - {type(n)}')