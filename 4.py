'''
Вводим 3 произвольных слова. Пусть будет название овощей.
Выводим все 3 слова с нижнем регистре, в верхнем регистре, потом только первый сивол в верхний(есть отдельная функция для этого)
Далее вводим кол-во каждого овоща.
После чего с помощью метода format выводим все данные в читаемом виде.
'''

vegetable1 = input("1 овощ: ")
vegetable2 = input("2 овощ: ")
vegetable3 = input("3 овощ: ")
vegl_1 = vegetable1.lower()
vegl_2 = vegetable2.lower()
vegl_3 = vegetable3.lower()
vegu_1 = vegetable1.upper()
vegu_2 = vegetable2.upper()
vegu_3 = vegetable3.upper()
vegt_1 = vegetable1.title()
vegt_2 = vegetable2.title()
vegt_3 = vegetable3.title()
vegetables1 = int(input("количество " + vegetable1 + ": "))
vegetables2 = int(input("количество " + vegetable2 + ": "))
vegetables3 = int(input("количество " + vegetable3 + ": "))
print("{} {} ({}, {})".format(vegetables1, vegl_1, vegu_1, vegt_1))
print("{} {} ({}, {})".format(vegetables2, vegl_2, vegu_2, vegt_2))
print("{} {} ({}, {})".format(vegetables3, vegl_3, vegu_3, vegt_3))