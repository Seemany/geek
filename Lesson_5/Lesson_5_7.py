import json
# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
sredniypribil = {}
obshiy = {}
srednyak = 0
kolvo_uspeshnih = 0
spisok = []
with open('Lesson_5_7.txt', encoding="UTF-8") as f_obj:
    for line in f_obj:
        line = line.strip()
        line = line.split()
        # print(line)
        intovoe3 = int(round(float(line[3])))  # А вдруг дробь
        intovoe2 = int(round(float(line[2])))
        pribil = intovoe2 - intovoe3
        if pribil > 0:  # Успешние компании и их средняк
            kolvo_uspeshnih += 1
            srednyak += pribil
            obshiy.update({line[0]: pribil})
        else:  # Те у которых все не ок)
            obshiy.update({line[0]: pribil})

    srednyak = srednyak / kolvo_uspeshnih
    srednyak = int(srednyak)
    sredniypribil.update({"average_profit": srednyak})
    spisok.append(obshiy)
    spisok.append(sredniypribil)
    with open('Lesson_5_7.json', 'w') as write_f:
        json.dump(spisok, write_f)

