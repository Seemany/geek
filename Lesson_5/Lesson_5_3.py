# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
do20k = []
zpvseh = []
with open('lesson_5_3.txt', encoding="UTF-8") as f_obj:
    for stroka in f_obj:
        stroka = stroka.strip()
        stroka = stroka.split(" ")
        zpvseh.append(int(stroka[1]))
        if int(stroka[1]) < 20000:
            do20k.append(stroka[0])
            familii = ', '.join(do20k)
    sumsred = sum(zpvseh)//len(zpvseh)
    print(f'ЗП меньше 20к  - {familii}\nСредняя зарплата всех сотрудников = {sumsred}')