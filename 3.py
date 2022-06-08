'''
3.Написать мини калькулятор.
В консоле ожидается ввод того символа, операцию которую мы будем выполнять.
Операции: +, -, /, *, возведение в степень, модуль, рандомное число, факториал и арккосинус.
В консоль вводим столько значений, сколько требуется для операции. Для рандомного, например, 0.
Выводим значение.
'''

import math
import random

arithmetic_operation = input("Введите арифметическое действие: ")

while arithmetic_operation != "end":
    if arithmetic_operation == "+":
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        print(number1 + number2)

    elif arithmetic_operation == "-":
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        print(number1 - number2)

    elif arithmetic_operation == "/":
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        if number2 != 0:
            print(number1 / number2)
        else:
            print("На 0 делить нельзя")

    elif arithmetic_operation == "*":
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        print(number1 * number2)

    elif arithmetic_operation == "**":  # Возведение в степень.
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        print(pow(number1, number2))

    elif arithmetic_operation == "||":  # Модуль числа.
        number1 = float(input("Введите число: "))
        print(abs(number1))

    elif arithmetic_operation == "0":  # Операция рандомное число, если нажать на ноль.
        print(random.randint(0, 1000))

    elif arithmetic_operation == "//":  # Деление без остатка.
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        if number2 != 0:
            print(number1 // number2)
        else:
            print("На 0 делить нельзя")

    elif arithmetic_operation == "%": # Деление по модулю (остаток от деления).
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        print(number1 % number2)

    elif arithmetic_operation == "n!":  # Факториал.
        number1 = int(input("Введите  число: "))
        print(math.factorial(number1))

    elif arithmetic_operation == "arccos":
        number1 = float(input("Введите число: "))
        number11 = number1 * math.pi / 180
        print(math.acos(number11))
    arithmetic_operation = input("Введите end, что бы закончить: ")