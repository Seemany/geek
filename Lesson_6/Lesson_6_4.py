# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

# Не использовал
#
# def __init__(self, naborspeed, color, name, is_police):
#     super().__init__(naborspeed, color, name, is_police)

#     так как нет своих личных атрибутов у дочерних классов


class Car():
    def __init__(self, naborspeed, color, name, is_police):
        self.speed = 0
        self.naborspeed = naborspeed  # Набор скорости скорость авто
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, timer):
        for sek in range(timer):
            self.speed = self.speed + self.naborspeed


    def stop(self, timer):
        for sek in range(timer):
            self.speed = self.speed - self.naborspeed
            if self.speed <= 0:
                self.speed = 0

    def turn(self, direction):
        print('__Поворот__')
        self.direction = direction
        if self.direction == 0:
            print('<--Влево')
        elif self.direction == 1:
            print('Вправо-->')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):

    limitspeed = 65

    def go(self, timer):
        for sek in range(timer):
            self.speed = self.speed + self.naborspeed
            if self.speed >= self.limitspeed:
                break



    def show_speed(self):
        print(f'Текущая скорость - {self.speed}')
        if self.speed > 60:
            print('Превышении скорости! Скорость ограничена!')
            # При значении скорости свыше 60 (TownCar)


class SportCar(Car):
    pass



class WorkCar(Car):

    limitspeed = 45

    def go(self, timer):
        for sek in range(timer):
            self.speed = self.speed + self.naborspeed
            if self.speed >= self.limitspeed:
                break


    def show_speed(self):
        print(f'Текущая скорость - {self.speed}')
        if self.speed > 40:
            # При значении скорости свыше 40(WorkCar)
            print('Превышении скорости! Скорость ограничена!')
            self.speed = 40

class PoliceCar(Car):
    # def __init__(self, naborspeed, color, name, is_police):
    #     super().__init__(naborspeed, color, name, is_police)

    def miymiy(self, timer):
        for sek in range(timer):
            print("Красный")
            print("Синий")


a = TownCar(10, 'Красный', 'Lincoln', False)
b = SportCar(30, 'Зеленый', 'Alfa Romeo', False)
c = WorkCar(5, 'Оранжевый', 'Камаз', False)
v = PoliceCar(30, 'Белый', 'Ford', True)
a1 = TownCar(20, 'Черный', 'VOLVO', False)


print(f'__________{a.name}__{a.color}__________')
a.go(5)
a.show_speed()
a.stop(1)
a.show_speed()
a.go(10)
a.show_speed()
a.stop(2)
a.show_speed()
a.turn(0)
a.go(8)
a.show_speed()
a.turn(1)

print(f'__________{a1.name}__{a1.color}__________')
a1.go(1)
a1.show_speed()
a1.stop(1)
a1.show_speed()
a1.go(10)
a1.show_speed()
a1.stop(2)
a1.show_speed()
a1.turn(0)
a1.go(8)
a1.show_speed()
a1.turn(1)


print(f'__________{c.name}__{c.color}__________')
c.go(3)
c.show_speed()
c.stop(2)
c.show_speed()
c.turn(0)
c.go(15)
c.show_speed()
c.stop(1)
c.show_speed()
c.turn(1)

print(f'__________{v.name}__{v.color}__________')
v.go(2)
v.show_speed()
v.stop(2)
v.show_speed()
v.turn(0)
v.go(8)
v.show_speed()
v.turn(1)
v.miymiy(1)
