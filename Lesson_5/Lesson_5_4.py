# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
ruschisla = ["Один", "Два", "Три", "Четыре"]
with open('Lesson_5_4_eng.txt', encoding='UTF-8', mode='r') as f_obj:
    for stroka in f_obj:
        stroka = stroka.strip()
        stroka = stroka.split()
        chislo = int(stroka[2])
        poruski = ruschisla[chislo-1]
        stroka[0] = poruski
        with open('Lesson_5_4_rus.txt', encoding='UTF-8', mode='a') as rus_obj:
            stroka = ' '.join(stroka)
            rus_obj.write(f'{stroka}\n')
        print(stroka)