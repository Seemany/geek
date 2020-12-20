# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('lesson_5_5.txt', encoding='UTF-8', mode='a') as f_obj:
    f_obj.write('1 2 3 4 5 11 66')

with open('lesson_5_5.txt', encoding='UTF-8', mode='r') as f_obj:
    contend = f_obj.read()
    contend = contend.split(" ",)
    for el in contend:
        el=int(el)
        el+=el
    print(f'Сумма чисел равна = {el}')