# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

mesyac = int(input("Введите месяц: "))

# list
if mesyac <= 2 or mesyac == 12:
    print("Это зима")
elif 6 > mesyac >= 3:
    print("Это весна")
elif 9 > mesyac >= 6:
    print("Это лето")
elif 12 > mesyac >= 9:
    print("Это осень")

# dict

mesyaci = {}
i = 1
while i < 13:
    if i <= 2 or i == 12:
        mesyaci[i] = "Зима"
    elif 6 > i >= 3:
        mesyaci[i] = "Весна"
    elif 9 > i >= 6:
        mesyaci[i] = "Лето"
    elif 12 > i >= 9:
        mesyaci[i] = "Осень"
    i += 1

print(f'Это {mesyaci.get(int(input("Введите число: ")))}')