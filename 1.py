# 1.Ввести произвольное число в консоле
# Ввести пограничное число в консоле
# Если 1ое число меньше пограничного, вывести сообщение об этом.
# Если 1ое число больше пограничного, вывести сообщение об этом.
# Если 1ое число больше пограничного более, чем в 3 раза, сообщить об этом.

first_number = int(input('First_number:'))
second_number = int(input('Second_number:'))

if first_number < second_number:
    print("First number is less than the second number")

elif first_number > second_number:
    print("First number is greater than the second number")

elif first_number * 3 > second_number:
    print("First number is 3 times larger than the second number")

else:
    print("Error.Try again!")
