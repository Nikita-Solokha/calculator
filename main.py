import math


class Calc:
    def __init__(self, values):
        self.values = values
        self.result = None

    def plus(self):
        self.result = sum(self.values)
        return self.result

    def minus(self):
        self.result = self.values[0]
        for value in self.values[1:]:
            self.result -= value
        return self.result

    def umnoj(self):
        self.result = 1
        for value in self.values:
            self.result *= value
        return self.result

    def delenie(self):
        if len(self.values) < 2:
            print("Ошибка: Для деления необходимо ввести как минимум два значения.")
            return None

        try:
            divisor = float(input("Введите значение, на которое хотите поделить: "))
            if divisor == 0:
                print("Ошибка: деление на ноль.")
                return None

            self.result = [value / divisor for value in self.values]
            return self.result

        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число.")

    def stepeni(self):
        if len(self.values) < 2:
            print("Ошибка: Для возведения в степень необходимо ввести как минимум два значения.")
            return None

        try:
            exponent = float(input("Введите значение степени: "))
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число для степени.")
            return None

        self.result = [value ** exponent for value in self.values]
        return self.result

    def koren(self):
        self.result = [math.sqrt(value) for value in self.values if value >= 0]
        if len(self.result) < len(self.values):
            print("Ошибка: не все значения положительные, корень не может быть вычислен.")
        return self.result


def user_vvod():
    try:
        values_input = input("Введите значения через пробел: ")
        values = list(map(float, values_input.split()))

        calc = Calc(values)

        print("Выберите операцию: ")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень ")
        print("6. Выделение квадратного корня из всех значений")

        vibor = input("Введите номер операции: ")

        if vibor == '1':
            print(f"Результат сложения: {calc.plus()}")
        elif vibor == '2':
            if len(values) < 2:
                print("Ошибка: Для вычитания необходимо ввести как минимум два значения.")
            else:
                print(f"Результат вычитания: {calc.minus()}")
        elif vibor == '3':
            print(f"Результат умножения: {calc.umnoj()}")
        elif vibor == '4':
            result = calc.delenie()
            if result is not None:
                print(f"Результат деления: {result}")
        elif vibor == '5':
            result = calc.stepeni()
            if result is not None:
                print(f"Результат возведения в степень: {result}")
        elif vibor == '6':
            print(f"Квадратные корни из значений: {calc.koren()}")
        else:
            print("Некорректный ввод номера операции.")

        repeat = input("Хотите выполнить еще одно действие? (да/нет): ")
        if repeat.lower() == 'да':
            user_vvod()

    except ValueError:
        print("Ошибка: Пожалуйста, введите числовые значения.")


user_vvod()
