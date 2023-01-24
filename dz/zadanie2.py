c = int(input("Введите число от 1 до 99: "))
if 1 <= c <= 99:
    print(c, end="")
    if (c % 10 == 1) and (c != 11):
        print(" Копейка")
    elif (c % 10 == 2) and (c != 12) or (c % 10 == 3) and (c != 13) or (c % 10 == 4) and (c != 14):
        print(" Копейки")
    # elif (c % 10 == 3) and (c != 13):
    #     print(" Копейки")
    # elif (c % 10 == 4) and (c != 14):
    #     print(" Копейки")
    else:
        print(" Копеек")
else:
     print("Не корректное значение")