class Car:
    def __init__(self, name, color, isPolice=False):
        self.name = name
        self.color = color
        self.is_police = isPolice
        self.speed = 0

    def go(self):
        print(f"{self.color} {self.name} двигается.")
        self.speed += 10

    def stop(self):
        print(f"{self.color} {self.name} остановился")
        self.speed = 0

    def turn(self, direction):
        print(f"{self.color} {self.name} повернул {direction}.")

    def showSpeed(self):
        print(f"Текущая скорость {self.color} {self.name}: {self.speed} км/ч.")

class TownCar(Car):
    def showSpeed(self):
        super().showSpeed()
        if self.speed > 60:
            print(f"ПРЕВЫШЕНА СКОРОСТЬ!")

class SportCar(Car):
    pass

class WorkCar(Car):
    def showSpeed(self):
        super().showSpeed()
        if self.speed > 40:
            print(f"ПРЕВЫШЕНА СКОРОСТЬ!")

class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, isPolice=True)

def outputMenu(chosenCar):
    print(f"Выберите действие:")
    print(f"1. Выбрать автомобиль (текущий: {chosenCar.name})")
    print(f"2. Поехать/Ускориться")
    print(f"3. Повернуть")
    print(f"4. Проверить скорость")
    print(f"5. Остановиться")
    print(f"6. Завершение программы")

townCar = TownCar("Volkswagen Polo", "Белый")
sportCar = SportCar("Lamborghini Huracan", "Красный")
workCar = WorkCar("Грузовик", "Черный")
policeCar = PoliceCar("Полицейский Бобик", "Синий")

chosenCar = townCar
while True:
    outputMenu(chosenCar)
    while True:
        try:
            choise = int(input())
        except ValueError:
            print(f"!ОШИБКА! Введено неправильное значение")
        else:
            if choise < 1 or choise > 6:
                print(f"!ОШИБКА! Выберете значение от 1 до 6")
            else: break
    match choise:
        case 1:
            print("Выберите автомобиль:")
            print(f"1. {townCar.name}")
            print(f"2. {sportCar.name}")
            print(f"3. {workCar.name}")
            print(f"4. {policeCar.name}")
            while True:
                try:
                    car = int(input())
                except ValueError:
                    print(f"!ОШИБКА! Введено неправильное значение")
                else:
                    if car < 1 or car > 4:
                        print(f"!ОШИБКА! Выберете значение от 1 до 4")
                    else:
                        break
            match car:
                case 1: chosenCar=townCar
                case 2: chosenCar=sportCar
                case 3: chosenCar=workCar
                case 4: chosenCar=policeCar
        case 2:
            chosenCar.go()
            chosenCar.showSpeed()
        case 3:
            print("Выберите сторону:")
            print(f"1. Влево")
            print(f"2. Вправо")
            while True:
                try:
                    directionChoise = int(input())
                except ValueError:
                    print(f"!ОШИБКА! Введено неправильное значение")
                else:
                    if directionChoise < 1 or directionChoise > 2:
                        print(f"!ОШИБКА! Выберете значение от 1 до 2")
                    else:
                        break
            if directionChoise == 1: direction = "Влево"
            else: direction = "Вправо"
            chosenCar.turn(direction)
        case 4: chosenCar.showSpeed()
        case 5: chosenCar.stop()
        case 6: break


