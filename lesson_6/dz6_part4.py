# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
            return f'машина {self.name} поехала'

    def stop(self):
            return f'\n машина {self.name} остановилась'

    def turn(self, direction):
            return f'\n машина {self.name} повернула {direction}'

    def show_speed(self):
            return f'\n скорость составляет {self.speed}'

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'\n ваша скорость {self.speed} больше разрешенной'
        else:
            return {self.speed}

class SportCar(Car):
    pass

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'ваша скорость {self.speed} больше разрешенной'
        else:
            return {self.speed}


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

town_car = TownCar(70, 'green', 'Mazda', False)
print(town_car.go(), town_car.turn('направо'), town_car.show_speed(), town_car.stop())
