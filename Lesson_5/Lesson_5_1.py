# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


while True:
    f = open('lesson5_1.txt', 'a', encoding="UTF-8")
    vvod = input("Введите данные: ")
    f.write(f'{vvod}\n')
    if vvod == "":
        break
    f.close()
