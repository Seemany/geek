# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

stroka = input("Введите строку: ")
razdel = stroka.split(" ")
i = 0
while i < len(razdel):
    if len(razdel[i]) >= 10:
        print(f'№{i}, {razdel[i][0:10:1]}')
    else: print(f'№{i}, {razdel[i]}')
    i += 1

# Или
# for ind, el in enumerate(razdel):
#     print(ind, el[0:10:1])