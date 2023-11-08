import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print("Алфавит:", self.letters)

    def lettersNum(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __lettersNum = 26

    def __init__(self):
        super().__init__('EN', string.ascii_uppercase)

    def isEnLetter(self, letter):
        return letter.upper() in self.letters

    def lettersNum(self):
        return self.__lettersNum

    @staticmethod
    def example():
        return "The example text in English"

def outputMenu():
    print(f"Выберите действие:")
    print(f"1. Вывод всех букв и их общее количество")
    print(f"2. Проверка буквы на принадлежность английскому языку")
    print(f"3. Вывод примера на английском языке")
    print(f"4. Завершение программы")

engAlphabet = EngAlphabet()
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
            engAlphabet.print()
            print(f"Количество букв в алфавите: {engAlphabet.lettersNum()}")
        case 2:
            letter = input("Введите букву\n")
            if letter.isalpha() == False:
                print("Введена не буква!")
            else:
                if len(letter) > 1:
                    print("Введено более одного символа!")
                else:
                    if engAlphabet.isEnLetter(letter) == True:
                        print(f"{letter} - буква английского алфавита")
                    else: print(f"{letter} - не является буквой английского алфавита")
        case 3: print(EngAlphabet.example())
        case 4: break