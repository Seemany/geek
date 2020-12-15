# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

# Во втором задании - просто пробегаетесь по списку и сравниваете  два рядом стоящих элемента.
# Если условие сравнения выполнено - добавляет элемент в результирующий список.
# Сделайте сначала просто циклом, а потом оформите в виде генараторного выражения.


spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# newspisok = []
# i=0
# for i in range(1, len(spisok),1):
#     if spisok[i-1] < spisok[i]:
#         newspisok.append(spisok[i])

newspisok = [spisok[i] for i in range(1, len(spisok), 1) if spisok[i - 1] < spisok[i]]

print(newspisok)
