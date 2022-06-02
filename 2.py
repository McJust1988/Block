name = input("Введите строку: ")
last_name = name[:-1]
start = -1
str_name = " "
for i in range(0, len(last_name)):
    if i != 2:
        str_name = str_name + last_name[i]
print(str_name)
if name.find("с") >= 0:
    print("содержится символ \"с\"")
