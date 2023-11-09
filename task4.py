class Car:
    totalCars = 0
    listOfCars = []

    def __init__(self, name, price, speed, acceleration):
        self.name = name
        self.price = price
        self.speed = speed
        self.acceleration = acceleration
        self.info = {'Название': self.name, 'Цена': self.price, 'Скорость (км/ч)': self.speed, 'Ускорение (м/с)': self.acceleration}
        Car.listOfCars.append(self.info)
        Car.totalCars += 1

    def testDrive(self):
        print(f"{self.name} набирает скорость {self.speed} км/ч при ускорении {self.acceleration} м/с за {self.speed/(3.6*self.acceleration)} с")

    @staticmethod
    def getTotalCars(Car):
        return Car.total_products

def outputMenu():
    print(f"Выберите действие:")
    print(f"1. Добавить автомобиль")
    print(f"2. Тест-драйв")
    print(f"3. Показать список всех автомобилей")
    print(f"4. Завершение программы")

while True:
    outputMenu()
    while True:
        try:
            choise = int(input())
        except ValueError:
            print(f"!ОШИБКА! Введено неправильное значение")
        else:
            if choise < 1 or choise > 4:
                print(f"!ОШИБКА! Выберете значение от 1 до 4")
            else: break
    match choise:
        case 1:
            while True:
                name = input("Название:")
                if name.replace(' ','') == '':
                    print('!ОШИБКА! Не введено название')
                else: break
            while True:
                try:
                    price = int(input("Цена:"))
                except ValueError:
                    print('!ОШИБКА! Введено не целое значение цены')
                else:
                    if price < 0:
                        print("!ОШИБКА! Цена не может быть отрицательной")
                    else: break
            while True:
                try:
                    speed = float(input("Скорость:"))
                    acceleration = float(input("Ускорение:"))
                except ValueError:
                    print('!ОШИБКА! Введено неправильное значение')
                else:
                    if speed <= 0 or acceleration <= 0:
                        print("!ОШИБКА! Скорость/цена не могут быть меньше или равны нулю")
                    else: break
            chosenCar=Car(name,price,speed,acceleration)
        case 2:
            if chosenCar.name is None:
                print('!ОШИБКА! Вы не выбрали машину')
            else: chosenCar.testDrive()
        case 3:
            for item in Car.listOfCars:
                print(item)
        case 4: exit()