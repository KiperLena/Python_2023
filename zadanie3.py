# задача №1
a = int(input("Введите количество символов: "))
b = input("Введите тип символа: ")
c = int(input("введите ориентацию линии : \n0- горизонтально \n1 - вертикально: "))
print()
i = 0
while i < a:
    if c == 0:
        print(b, end="")
        i += 1
    if c == 1:
        print(b)
        i += 1

# задача №2

# a = input("Введите любой символ: ")
# b = input("Введите второй любой символ: ")
# print()
# i = 0
# while i < 2:
#     print(a*16)
#     j = 0
#     while j < 1:
#         print(b*16)
#         j += 1
#     i += 1

# задача №3

# a = int(input("Введите любое число: "))
# b = int(input("Введите любое число: "))
# c = int(input("Введите любое число: "))
# print(a, b, c)
#
# maxim = a if a > b  and a > c else b if b > a and b > c else c
# print(maxim)

#или:

# i = 1
# ch = int(input("Введите любое число: "))
# maxim = ch
# while i < 3:
#     ch = int(input("Введите любое число: "))
#     if ch > maxim:
#         maxim = ch
#     i += 1
#
# print("Максимальное число: ", maxim)

#или:

# i = 1
# ch = int(input("Введите любое число: "))
# maxim = ch
# while True:
#     ch = int(input("Введите любое число: "))
#     if i == 2:
#         break
#     i +=1
#     if ch > maxim:
#         maxim = ch
# print("Максимальное число: ", maxim)

# задача №4

# print("1 - "r" - применяет унарный минус к операнду " "\n2 - сложение"
#       "\n3 - вычитание"  "\n4 - деление"  "\n5 - умножение"  "\n6 - деление по модулю "
#       "(остаток от деления)" "\n7 - минимальное из двух чисел"  "\n8 - максимальное из двух чисел")
# print()
# c = int(input("Введите цифру операции от 1 до 8: "))
# print()
# if c == 1:
#     a = int(input("Введите число: "))
#     a *= -1
#     print("Результат:", a)
# elif c == 2:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     a = a + b
#     print("Результат сложения:", a)
# elif c == 3:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     a = a - b
#     print("Результат вычитания:", a)
# elif c == 4:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     d = a / b if b != 0 else "На ноль делить нельзя"
#     print("Результат деления:", d)
# elif c == 5:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     a = a * b
#     print("Результат умножения:", a)
# elif c == 6:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     a = a % b
#     print("Результат остаток от деления:", a)
# elif c == 7:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     if a < b:
#         print("Минимальное число: ", a)
#     elif b < a:
#         print("Минимальное число: ", b)
#     else:
#         print("Равные числа ")
# elif c == 8:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     if a > b:
#         print("Максимальное число: ",a)
#     elif b > a:
#         print("Максимальное число: ", b)
#     else:
#         print("Равные числа ")




