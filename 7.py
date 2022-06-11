# Сделать из функций калькулятора отдельный класс.
import math
import random


class Calculator:
    def plus(self, number1, number2):
        return number1 + number2

    def minus(self, number1, number2):
        return number1 - number2

    def div(self, number1, number2):
        if number2 != 0:
            return number1 / number2
        else:
            print("на 0 делить нельзя")

    def multi(self, number1, number2):
        return number1 * number2

    def pow(self, number1, number2):
        return math.pow(number1, number2)

    def module(self, number1):
        return abs(number1)

    def rand(self, number1, number2):
        return random.uniform(number1, number2)

    def whole_div(self, number1, number2):
        if number2 != 0:
            return number1 // number2
        else:
            print("на 0 делить нельзя")

    def mod(self, number1, number2):
        return number1 % number2

    def factorial(self, number1):
        return math.factorial(number1)

    def arccos(self, number1):
        return number1 * math.pi / 180


calc = Calculator()
do = input("Введите арифметическое действие: ")
while do != "end":
    if do == "+":
        print(calc.plus(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "-":
        print(calc.minus(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "/":
        print(calc.div(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "*":
        print(calc.multi(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "**":  # Возведение в степень.
        print(calc.pow(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "||":  # Модуль числа.
        print(calc.module(number1=float(input("Введите число: "))))

    elif do == "0":  # Операция рандомное число, если нажать на ноль.
        print(
            calc.rand(number1=float(input("Введите верхнее число: ")), number2=float(input("Введите нижнее число: "))))

    elif do == "//":  # Деление без остатка.
        print(calc.whole_div(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "%":  # Деление по модулю (остаток от деления).
        print(calc.mod(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "n!":  # Факториал.
        print(calc.factorial(number1=int(input("Введите число: "))))

    elif do == "arccos":
        print(math.acos(calc.arccos(number1=float(input("Введите число: ")))))

    do = input("Введите end, что бы закончить: ")
