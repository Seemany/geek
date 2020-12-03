# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

perm_int = 10
perm_str = '10'
perm_float = 1.4
perm_bool = type(True)
print(perm_int, perm_str, perm_float, perm_bool)
vvod_chisla = input('Введите числа: ')
if vvod_chisla.isdigit():      # проверка на число
    print('Спасибо что ввели число =)')
else:
    print('Вы ввели не число =( ну ладненько')

print(vvod_chisla)
vvod_stroki = input('Введите строку: ')
print(vvod_stroki)

vvod_chisla1 = input('Введите числа: ')
if vvod_chisla1.isdigit():  # проверка на число
    print('Спасибо что ввели число =)')
else:
    print('Вы ввели не число =( ну ладненько')

print(vvod_chisla1)
vvod_stroki1 = input('Введите строку: ')
print(vvod_stroki1)


#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

vvod_vremeni = int(input('Введите секунды: '))
chas = 0
minuta = 0
sek = 0
if vvod_vremeni >= 1:
    chas = vvod_vremeni // 3600
    if chas >= 1:
        ostchas = (vvod_vremeni % 3600)
        if ostchas >= 1:
            minuta = ostchas // 60
            sek = ostchas % 60
    else:
        minuta = vvod_vremeni // 60
        sek = vvod_vremeni % 60
else:
    print('Вы ввели отрицательное число')

print(f"{chas}:{minuta}:{sek}")

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите n')
n1 = n * 2
n2 = n * 3
print(int(n) + int(n1) + int(n2))

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

vvod_chisla = input("Введите число")
kolvo_elem = len(vvod_chisla)
i = 0
maks_chislo = 0
while i < kolvo_elem:
    perevod_int = int(vvod_chisla[i])
    if perevod_int > maks_chislo:
        maks_chislo = perevod_int
    i = i + 1
print(maks_chislo)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

vvod_viruchka = int(input("Введите выручку"))
vvod_izderjki = int(input("Введите издержки"))
pribil = vvod_viruchka - vvod_izderjki

if vvod_viruchka > vvod_izderjki:
    print(f'Выручка больше издержек, общая прибыль {pribil}')
    rentabelnost = (pribil / vvod_viruchka)*100
    print(f'Коэффициент рентабельности продаж (ROS): {rentabelnost} ; Рентабельность продаж: {rentabelnost}%')
else:
    ybitok = vvod_viruchka - vvod_izderjki
    print(f'Издержки больше выручки: {ybitok}')

vvod_sotrud = int(input("Введите число сотрудников:"))
nasotr = pribil//vvod_sotrud
print(f'На сотрудника: {nasotr}')

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

perviy_den = int(input("Введите результат первого дня"))
itog_den = int(input("Введите какой хотите результат"))
i = 1
print(f"\nРезультат:\n\n{i}-й день: {perviy_den}")
while perviy_den < itog_den:
    perviy_den = perviy_den + (perviy_den * 0.1)
    i = i + 1
    print(f'{i}-й день: {str(perviy_den):1.4}')

print(f'Ответ: на {i}-й день спортсмен достиг результата — не менее {itog_den} км.')

