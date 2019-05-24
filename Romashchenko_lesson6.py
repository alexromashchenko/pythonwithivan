

# Задача - 1 (СДЕЛАНО)
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
# Задача - 2 (СДЕЛАНО)
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class TownCar:
    def __init__(self, car):
        self.speed = 60
        self.color = 'white'
        self.name = car
        self._is_police = False

    def go(self):
        print(f'the car is driving with {self.speed} m/p/h')

    def stop(self):
        print('The car has been stopped')

    def turn_direction(self):
        print('The car is turning left or right')

town_car = TownCar('toyota')
print(town_car.color)

class SportCar(TownCar):
    def __init__(self,car):
        super(). __init__(car)
        self.speed = 200
        self.color = 'red'

sport_car = SportCar('lamborgini')
print(sport_car.speed)
print(sport_car._is_police)

class WorkCar(TownCar):
    def __init__(self,car):
        super(). __init__(car)
        self.speed = 30
        self.color = 'blue'

work_car = WorkCar('truck')
print(work_car.speed)
print(work_car.color)
print(work_car.go)

class PoliceCar(TownCar):
    def __init__(self,car):
        super(). __init__(car)
        self.speed = 90
        self.color = 'black and white'
        self._is_police = True

police_car = PoliceCar('crown_victoria')
print(police_car.speed)
print(police_car.color)
print(police_car.go)
print(police_car._is_police)

# Здесь так и не разобрался почему, например, print(police_car.go) возвращает закую-то фигню, а не то, что задумано.