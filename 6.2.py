#Переделываем задачу номер 4(про овощи) на функции.

def vegetLower(name):
    return name.lower()

def vegetUpper(name):
    return name.upper()

def vegetTitle(name):
    return name.title()

def sum(count):
    return count

vegetable1 = input("1 овощ: ")
vegetable2 = input("2 овощ: ")
vegetable3 = input("3 овощ: ")

vegetables1 = int(input("сколько " + vegetable1 + ": "))
vegetables2 = int(input("сколько " + vegetable2 + ": "))
vegetables3 = int(input("сколько " + vegetable3 + ": "))

print('{} {}({}, {})'.format(sum(vegetables1), vegetLower(vegetable1), vegetUpper(vegetable1), vegetTitle(vegetable1)))
print('{} {}({}, {})'.format(sum(vegetables2), vegetLower(vegetable3), vegetUpper(vegetable2), vegetTitle(vegetable2)))
print('{} {}({}, {})'.format(sum(vegetables3), vegetLower(vegetable3), vegetUpper(vegetable3), vegetTitle(vegetable3)))