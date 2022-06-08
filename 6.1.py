# 6.Переделываем задачу номер 3(калькулятор) на функции.

import math
import random


def plus(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def division(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        print("на 0 делить нельзя")

def multiplication(number1, number2):
    return number1 * number2

def pow(number1, number2):
    return math.pow(number1, number2)

def module(number1):
    return abs(number1)

def rand(number1, number2):
    return random.uniform(number1, number2)

def division_without_remainder(number1, number2):
    if number2 != 0:
        return number1 // number2
    else:
        print("на 0 делить нельзя")

def division_by_modulus(number1, number2):
    return number1 % number2

def factorial(number1):
    return math.factorial(number1)

def arccos(number1):
    return number1 * math.pi / 180


arithmetic_operation = input("Введите арифметическое действие: ")
while arithmetic_operation != "end":
    if arithmetic_operation == "+":
        print(plus(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif arithmetic_operation == "-":
        print(minus(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif arithmetic_operation == "/":
        print(division(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif arithmetic_operation == "*":
        print(multiplication(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif arithmetic_operation == "**":  # Возведение в степень.
        print(pow(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif arithmetic_operation == "||":  # Модуль числа.
        print(module(number1=float(input("Введите число: "))))

    elif arithmetic_operation == "0":  # Операция рандомное число, если нажать на ноль.
        print(rand(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif arithmetic_operation == "//":  # Деление без остатка.
        print(division_without_remainder(number1=float(input("Введите 1 число: ")),
                                         number2=float(input("Введите 2 число: "))))

    elif arithmetic_operation == "%":   # Деление по модулю (остаток от деления).
        print(division_by_modulus(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif arithmetic_operation == "n!":  # Факториал
        print(factorial(number1=float(input("Введите число: "))))

    elif arithmetic_operation == "arccos":
        print(math.acos(arccos(number1=float(input("Введите число: ")))))

    arithmetic_operation = input("Введите оператор: ")
