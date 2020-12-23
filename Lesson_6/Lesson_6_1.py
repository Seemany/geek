import time


# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.


class TrafficLight():
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def running(self, vvod):
        self.vvod = vvod
        if self.vvod == self.__color[0]:
            self.__rubilnik = 0
        elif self.vvod == self.__color[1]:
            self.__rubilnik = 1
        else:
            self.__rubilnik = 2
        print("Чтобы остановить светофор комбинация клавиш Ctrl+C")
        while True:
            try:
                if self.__rubilnik == 0:
                    self.__rubilnik += 1
                    print('Красный')
                    time.sleep(7)
                elif self.__rubilnik == 1:
                    self.__rubilnik += 1
                    print('Желтый')
                    time.sleep(2)
                elif self.__rubilnik == 2:
                    self.__rubilnik += 1
                    print('Зеленый')
                    time.sleep(2)
                    self.__rubilnik = 0
            except KeyboardInterrupt:
                    print(" Стоп светофор")
                    break

a = TrafficLight()
a.running('зеленый')

# Не то похоже

# class TrafficLight():
#     __color = 0
#
#     def runnig(self, vvod):
#         self.vvod = vvod.lower()
#         if self.vvod == 'красный':
#             self.__color = 0
#         elif self.vvod == 'желтый':
#             self.__color = 1
#         elif self.vvod == 'зеленый':
#             self.__color = 2
#         print("Чтобы остановить светофор комбинация клавиш Ctrl+C")
#         while True:
#             try:
#                 if self.__color == 0:
#                     self.__color += 1
#                     print('Красный')
#                     time.sleep(7)
#                 elif self.__color == 1:
#                     self.__color += 1
#                     print('Желтый')
#                     time.sleep(2)
#                 elif self.__color == 2:
#                     self.__color += 1
#                     print('Зеленый')
#                     time.sleep(1)
#                     self.__color = 0
#             except KeyboardInterrupt:
#                 print(" Стоп светофор")
#                 break
#
# a = TrafficLight()
# a.runnig('желтый')
