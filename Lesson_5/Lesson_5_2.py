# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

kolvostr = 0
with open("lesson_5_2.txt", encoding="UTF-8") as f_obj:
    for stroka in f_obj:
        kolvostr+=1
        razbiv = stroka.split(" ")
        kolvoslov = len(razbiv)
        print(f'В строке № {kolvostr} слов {kolvoslov}')
