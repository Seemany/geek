# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
    def __str__(self):
        return f'{self.txt}'

inp_data = int(input('Первое число '))
inp_data2 = int(input('Второе число '))

try:
    inp_data = int(inp_data)
    inp_data2 = int(inp_data2)

    z = inp_data / inp_data2

except ZeroDivisionError:
    c = OwnError('Была ошибка')
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {z}")

# print(c)