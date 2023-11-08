class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y != 0:
            self.result = x / y
        else:
            self.result = "!ОШИБКА! Деление на ноль"

    def getResult(self):
        return self.result

def getInput():
    try:
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))
        return x, y
    except ValueError:
        print("!ОШИБКА! Введены не числовые значения")
        return None, None


calculator = Calculator()
while True:
    operation = input("Выберите операцию (+, -, *, /):\n(Для выхода введите EXIT) \n").strip()
    if operation.upper() == "EXIT":
        exit()
    if operation in ('+', '-', '*', '/'):
        x, y = getInput()

        if x is not None and y is not None:
            if operation == '+':
                calculator.add(x, y)
            elif operation == '-':
                calculator.subtract(x, y)
            elif operation == '*':
                calculator.multiply(x, y)
            elif operation == '/':
                calculator.divide(x, y)

            result = calculator.getResult()
            print(f"Результат: {result}")
    else:
        print("!ОШИБКА! Такой операции не существует")
