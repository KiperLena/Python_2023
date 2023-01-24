# name1 = "Elena"
# age = 20
# print("Hello,", name1)
# print(type(age))
import random

# a = b = c = 1
# print(a, b, c)

# a, b, c = "Hello", 5, False
# print(a, b, c)

# a = "Hello"
# print(a)
# print(type(a))
# a = 5
# print(type(a))

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# name = "Olga"
# age = 21
# print("Меня зовут " + name + ".Мне " + str(age) + " лет")

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a, b = b, a
# c = a
# a = b
# b = c
# c = a
# a = a - a + b
# b = b - b + c
# или
# c = a + b
# a = c - a
# b = c - b
# или
# a = a + b
# b = a - b
# a = a - b
# print("a:", a)
# print("b:", b)

# print(" строка \
#       символов")
# print(' строка символов ')

# print("Документ \"file.py\" наъодится по заданному"
#       " пути \t\t\t\t\tC:\\User\\Вениамин\\Desktop"
#       "\\Пайтон\\file.py")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3)
# print(s3 * 3)

# print(445454622452111222233522)
# print(4.45454622452111222567722)
#
# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 5)
# print(6 // 5)
# print(6 % 4)
# print(7 ** 2)


# a = 5
# b = 7
# c = 3
# summa = a + b + c
# proiz = a * b * c
# sred = summa/3
# print("Сумма:", summa)
# print("Произведение:", proiz)
# print("Среднее:", sred)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5  # num = num + 5 = 10+5
# print(num)
#
# num -= 3
# print(num)  # 12
#
# num *= 4  # num=num*4 = 12*4
# print(num)


# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10
# print(num)
# c = num % 10
# print(c)
# num = num // 10
# print(num)
# d = num % 10
# print(d)
# print(a, b, c, d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = (num % 10) * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)


# num1 = "2"
# num2 = 3
# res = num1 + str(num2) #23
# res = int(num1) + num2 #5
# print(res)
#
# print(int(3.8))
# a = 3.8
# print(type(round(a)))
#
# print(round(3.491, 2))

# print(6 / 2)

# num1 = "2.5"
# num2 = 3
# res = float(num1) + num2
# print(res)

# a = 1
# b = 2
# print("a:", a, "\nb:", b)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="__", end="%")
#
# print("Я учу Python.")

# name = input("Введите имя: ")
# print("Hello", name)

# num = int(input("Введите любое число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно: ", res)

# print(bool("python"))
# print(bool(""))
# print(bool(0)) #False
# print(bool(None)) #False
# print(bool(False)) #False
#
#
# test = None
# print(test)
# test = 5
# print(test)


# print(2<4<9) #true
#
# print(2 * 5 > 7 >= 4+3) #true
# print(3*3 <=7 <=2) #false

# a = 10
# b = 5
# c = a == b
# print(a,b,c)

# print(5-3 == 2 and 1+3 == 4)  #True
# print(5-4 == 2 and 1+3 == 4)  #False
#
# print(5-3 == 2 or 1+3 == 4)  #True
# print(5-4 == 2 or 1+3 == 4)  #False

# print(not 9 - 5) #False
# print(not 7 - 7)  #True
#
# cnt = 15
# if cnt < 10:
#     cnt +=1
# print(cnt)

# age = int(input("Введите свой возраст:"))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 25
# b = 15
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("a == b")

# a = int(input("Введите длину:"))
# b = int(input("Введите длину:"))
# c = int(input("Введите длину:"))
#
# if a == b == c:
#     print("равносторонний")
# elif a == b  or a == c or b == c:
#     print("равнобедренный")
# else:
#     print("разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if (day >= 1) and (day <= 5):   #1 <= day <= 5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# m = int (input("Введите месяц (цифрой): "))
# if 3 <= m <= 5:
#     print("Весна")
# elif 6 <= m <= 8:
#     print("Лето")
# elif 9 <= m <= 11:
#     print("Осень")
# else:
#     print("Зима")
#     if m > 12 or m < 1:
#         print("Такого месяца нет")

# m = int (input("Введите месяц (цифрой): "))
# if 1 <= m <= 12:
#     if 3 <= m <= 5:
#         print("Весна")
#     if 6 <= m <= 8:
#         print("Лето")
#     if 9 <= m <= 11:
#         print("Осень")
# else:
#     print("Зима")
#     if m > 12 or m < 1:
#         print("Такого месяца нет")

# c = int(input("Ввести количество ворон: "))
# if 0 <= c <=9:
#     print("На ветке", c, end="")
#     if c == 1:
#         print("ворона")
#     elif 2 <= c <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("не корректно")

# a, b = 10, 20
# minimum = a if a < b else b
# print(minimum)

# a, b = 30, 20
# minimum = "a == b" if a == b else "a > b" if a > b else "b > a"
# print(minimum)
# a, b = 10, 2
# c = a/b if b != 0 else "На ноль делить нельзя"
# print(c)

# Исключения

# try:
#     n = int(input("Введите целое число"))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое"))
#     m = int(input("Введите делитель"))
#     print(n / m)
# except ValueError :
#     print("Что-то пошло не так")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# try:
#       n = int(input("Введите делимое"))
#       m = int(input("Введите делитель"))
#       print(n / m)
# except (ValueError, ZeroDivisionError):
#       print("Нельзя вводить строки или делить на нуль")
# else:
#       print("Все хорошо. вы ввели", n, "и", m) #отработает когда except не работает
# finally:
#       print("Конец программы")

# n = input("Введите число")
# m = input("Введите число")
# try:
#       n = int(n)
#       m = int(m)
# except ValueError:
#       n = str(n)
# finally:
#       print(n + m)

# Циклы:

# while усоловие:
#      тело цикла

# i = 0
# while i < 5:
#       print("i =", i)
#       i +=1 #i = i + 1

# i = 10
# while i > 0:
#       print("i =", i)
#       i -= 1  # i = i + 1

# i = 1
# while i < 21:
#       if i % 2 == 0:
#           print("i = ", i)
#       i +=1

# i = 1
# while i < 21:
#       print(i + 1)
#       i += 2

# n = int(input("Укадите количество символов: "))
# i = 0
# while i < n:
#       print("*", end="")
#       i += 1

# n = int(input("Укадите количество символов: "))
# while n > 0:
#       print("*", end="")
#       n -= 1

# start = int(input('Start: '))
# end = int(input('End: '))
# i = start
# sum_ = 0
# while i <= end:
#     if i % 2:
#         sum_ += i
#     i += 1
# print('Summa:', sum_)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#       try:
#             n = int(n)
#       except:
#             print("Число не целое")
#             n = input("Введите целое число: ")
# if n % 2 == 0:
#       print("Четное число")
# else:
#       print("Нечетное число")

# i = 0
# while i < 10:
#       print(i, end="")
#       if i == 5:
#             break
#       i += 1
# print("\nЦикл завершен")

# i = 0
# while i < 10:
#       if i == 5:
#             i += 1
#             continue
#       print(i, end="")
#       i += 1
# print("\nЦикл завершен")


# i = 0
# while True:
#       print(i)
#       if i == 5:
#             break
#       i += 1

# while True:
#       n = int(input("Введите положит число:"))
#       if n < 0:
#             break
# print("Цикл завершен")


# mult = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     mult *= n
#
# print("Произведение:", mult)

# i = 0
# while i < 10:
#       if i == 5:
#             break
#       print(i)
#       i += 1
# else:
#       print("Цикл окончен, i=", i)

# kol = int(input("Введите количество чисел последовательности: "))
# i = 1
# ch = float(input("Введите число: "))
# min_ch = ch
# max_ch = ch
# sum_ch = ch
# while i < kol:
#     ch = float(input("Введите число: "))
#     sum_ch += ch
#     if ch < min_ch:
#         min_ch = ch
#     if ch > max_ch:
#         max_ch = ch
#     i += 1
# print("Количество чисел : ", kol)
# print("Минимальное число: ", min_ch)
# print("Максимальное число: ", max_ch)
# print("Среднеарифметическое число: ", sum_ch/kol)

# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1

# for in

# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'green', 1, 20, :
#     print("color: ", color)

# print(range(1, 3))

# for i in range(100, 0, -10):
#     print(i, end=" ")
# print()
# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 3

# a = int(input("Введите целое чисело: "))
# for i in range(1, a+1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")

# for i in range(1, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("-----", j)

# w = int(input("Введите Длину прямоугольника: "))
# h = int(input("Введите Ширну прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# w = int(input("Введите Длину прямоугольника: "))
# h = int(input("Введите Ширну прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h-1 or j == 0 or j == w-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# letter = [i for i in "Hello"]
# print(letter)

# num = [i for i in range(30) if i % 10 == 0]
# print(num)

# СПИСКИ
# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(id(nums))
# print(type(nums))
# print(nums[0])
# print(nums[2])
# print(nums[-1])
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)
# print(id(nums[3]))

# nums = [8, 3, 9, 4, 1]
# # print(nums)
# # print("Длина списка: ", len(nums))

# s = []    #создать список
# print(s)
#
# s1 = list()   #создать список
# print(s1)
#
# s2 = list("Hello")  #создать список
# print(s2)

# s = [1, 3, 5]
# print(s)
# n = s * 6
# print(n)

# n = list(range(2, 10, 3))
# print(n)

# n = 5
# a = [i**2 for i in range(1,n+1)]
# print(a)

# c = [i*3 for i in "list"]
# print(c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = c * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# print(a)
# a = [8, 4, 6, 5, 0]
#
# for i in range(len(a)):
#     print(a[i], end="")
# print()
# for elem in a:
#     print(elem, end="")

# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
#
# for i in a:
#     if i < 0:
#         s += i
#
# print("Сумма отрицательных элементов: ", s)

# sp = list(range(21,41))
# print(sp)
# ch = 0
# nech = 0
# for i in sp:
#     if i % 2 == 0:
#         ch += i
#     else:
#         nech += i
# print(ch)
# print(nech)

# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# # print(a)
# # n = 0
# # summa = 0
# # for i in a:
# #     summa += i
# #     if i != 0:
# #         n +=1
# # print(summa/n)

# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# print(a)
# # for i in range(1,len(a)):
# #     if a[i] > a[i-1]:
# #         print(a[i], end=" ")
# for i in a:
#     if i > a[i-1]:
#         print(i, end=" ")

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# a = [7, 8, 2, 1, 17, 5]
# print(a[1:4])
# print(a[::2])
# print(a[-2::-1])
# print(a[1:4:-1])
# print(a[10])

# s = list(range(1,8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[0:1:1])
# print(s[-1::])
# print(s[3:4:])
# print(s[4::1])
# print(s[4:1:-1])
# print(s[2:5:])

# a = [7, 8, 2, 1, 17, 5]
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = [50]
# print(a)
# del a[2]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)

# print(dir(list))
# s = [7, 8, 2, 1, 17, 5]
# print(s)
# s.append(99)
# print(s)
# s.extend([1, 2, 3])
# print(s)
# s.extend('add')
# print(s)
# s.insert(2, 100)
# print(s)

a = [1, 4, 2]
# n = int(input("n = "))
# for i in range(n):
#     # x = input("->")
#     # a.append(x)
#
#     a.append(input("->"))
# print(a)

# [a.append(input("->")) for i in range(int(input("n = ")))]
# print(a)

# a = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("->"))
#     if x%3 == 0:
#         a.append(x)
#     else:
#         print("не кратно")
#     #a.append(x) if not x % 3 else print(f'Число {x} не делится на 3 без остатка')
# print(a)

# a = [1, 2, 3, 2 ,6, 78, 2,44]
# b = [11, 22, 33, 2 ,4]
# c = []
# print(a)
# print(b)
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):   #range (3,5) от 3 до 5 длины списка
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(b[i])
#         c.append(a[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#
# print(c)

# a = [11, 1, 22, 2, 33, 3, 2, 2, 4, 6, 78, 2, 44]
# a.remove(2)
# print(a)
# a.pop()
# # last = a.pop()
# # print(last)
# print(a)
# last = a.pop(-2)
# print(last)
# print(a)
# a.clear()
# print(a)

# a = []
# [a.append(input("->")) for i in range(int(input("n = ")))]
# print(a)
# while True:
#     if len(a) == 0:
#         break
#     k = int(input("Введите индекс: \nk = "))
#     a.pop(k)
#     print(a)

# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: ")))]
# k = int(input("Введите индекс: "))
# a.pop(k)
# print(a)

# a = [5, 6, 7, 6]
# s = 0
# for i in a:
#     s += i
#
# print(s)

# a = [5, 6, 8, 9, 2, 9, 2, 9]
# print(a)
# num = a.count(9)
# print(num)
# ch = 9
# if ch in a:
#     ind = a.index(ch)
#     print(ind)

# a = [5, 6, 8]
# b = a.copy()
# print("a= ", a)
# print("b= ", b)
# b.append(120)
# print("a= ",a)
# print("b= ", b)
# print(id(a))
# print(id(b))


# a = [5, 6, 8, 9, 2, 9, 2, 9]
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
#
# s = ['Витя', 'Виталя', 'Александра', 'Лия']
# s.sort(key=len, reverse=True)
# print(s)
# s.sort(reverse=True)
# print(s)
#
# b = sorted(a)
# print(b)
# print(a)

# Генерация случайного числа:

# import random
#
# print(random.random())
# print(random.randint(0,9))
# print(random.randrange(9))
# print(random.randrange(0,9,2))

# from random import *
#
# print(randint(1,9))
# print(randrange(9))

import random as r

# print(r.randint(1, 9))
# print(r.randrange(9))
# print(r.uniform(10.5, 25.5))
#
# # city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# city = [2, 3, 4, 8, 6, 5, 6]
# print(r.choice(city))
# print(r.choices(city, k=3))
# r.shuffle(city)
# print(city)

# mas = [r.randint(1, 20) for i in range(5)]
# print(mas)

# lst = [3, 6, 12, 13, 1]
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# mas = [r.randint(1, 20) for i in range(10)]
# print(mas)
# b = max(mas)
# print(b)
# mas.remove(b)
# mas.insert(0, b)
# print(mas)

# mas = [r.randint(-10, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# mas = [r.randint(1, 20) for i in range(10)]
# print(mas)
# b = min(mas)
# print(b)
# c = mas.index(b)
# print(c)
# mas = mas[c:]
# print(mas)

# x = list('jjhf6yhogg7')
# print(x)
# print('j' not in x)
# print('x' not in x)
#
# lst = []
# if len(lst) == 0:
#     print("список пустой")
# if  not len:
#     print("список пустой")

# n1 = int(input("Ddtlbnt 1 cgbd"))
# n2 = int(input("Ddtlbnt 2 cgbd"))
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for i in range(n2)]
# print("первый списк:", a)
# print("2 списк:", b)
# c = a+b
# print(c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print(c)
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1,2,3,4,58],
#     [5,6,7,8],
#     [9,10,11,12,2,5]
# ]
# print(m)
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# print(m)
# for row in m:
#     for x in row:
#         print(x**2, end="\t")
#     print()

# w, h = 10, 10
# matrix = [[x*y for x in range(1, w)] for y in range(1, h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x+y)
# import random
#
# n = int(input("Размерность матрицы: "))
# mas = []
# for i in range(n):
#     mas.append([])
#     for j in range(n):
#         mas[i].append(random.randint(1, 100))
# print(mas)
# for row in mas:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# m = 101
# lst = []
# for k in range(n):
#     if m > mas[k][k]:
#         lst.append(mas[k][k])
# print(lst, end="\t")
# print("\n", min(lst))

# import math
# num1 = math.ceil(3.2)
# num2 = math.floor(3.8)
# num3 = math.sqrt(3.8)
#
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)

# from math import pi

# num1 = ceil(3.2)
# print(num1)

# import math as m

# r = int(input("Радиус окружности: "))
# print(2 * pi * r)

import time

# second = time.time()
# print(second)
# a = 175634931
# local_time = time.ctime(a)
# print(local_time)
# res = time.localtime()
# print(res)
# print(res.tm_year, res.tm_hour)
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %I:%M:%S", time.localtime(a)))

# pause = 2
# print("Запуск программы")
# time.sleep(pause)
# print(pause, "секунд")

# text = input("Название напоминания:")
# # locale_time = float(input("Через сколько минут: "))
# # locale_time = locale_time * 60
# # time.sleep(locale_time)
# # print(text)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня %B %d, %Y"))

# ФУНКЦИИ
# a = 20
#
#
# def hello(name, age):
#     print("Hello,", name, ". I am ", age, sep="")
#
#
# hello("Irina", 20)
# hello("Elena", 23)

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', 'hello')
# get_sum(5.2, 2.1)

# def func(n, a, b):
#     for i in range(n):
#         if i%2:
#             print(b, end='')
#         else:
#             print(a, end='')
#     print()
#
#
# func(9, "+", "-")
# func(9, "X", "0")
#
# func(n, a, b)
# def func(n, a, b):
#     [print(b, end='') if i % 2 else print(a, end='') for i in range(n)]
#     print()

# def get_sum(a, b):
#     if a > b:
#         return True
#     else:
#         return False
#
# x = 15
# y = 7
# if get_sum(x, y):
#     print("Первое число больше")
# else:
#     print("Второе число больше")


# def get_sum(a, b):
#     if a > b:
#         return True
#     else:
#         return False
#
#
# x = int(input(" Введите число:"))
# y = int(input(" Введите число:"))
# if get_sum(x, y):
#     print(x - y)
# else:
#     print(x + y)


# def cube(a):
#     return a ** 3
#
# for i in range(1, 11):
#     print(i, "в кубе = ", cube(i))

# def change(lst):
#     # lst[-1], lst[0] = lst[0], lst[-1]
#     n = lst.pop()
#     m = lst.pop(0)
#     lst.insert(0, n)
#     lst.append(m)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if 'a' <= ch <= "z":
#             has_lower = True
#         if '0' <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def place_rect(a, b):
#     print("Площадь прямоугольника = ", a * b)
#
#
# x = int(input(" Введите значение одной стороны прямоугольника:"))
# y = int(input(" Введите значение второй стороны прямоугольника:"))
# place_rect(x, y)
#
# print()
#
#
# def place_triangle(a, b):
#     print("Площадь треугольника = ", 0.5 * a * b)
#
#
# x = int(input(" Введите значение основания треугольника:"))
# y = int(input(" Введите значение высоты треугольника:"))
# place_triangle(x, y)
#
# print()
#
#
# def place_circle(a):
#     pi = 3.14
#     print("Площадь круга = ", pi * a**2)
#
#
# x = int(input(" Введите значение радиуса круга:"))
# place_circle(x)


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 3))
# print(get_sum(1, 2, 5))
# print(get_sum(1, 5))
# print(get_sum(1, 2, d=2))

# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()
#
# set_param(s="+")
# set_param(5, "*")
# set_param(7)
# set_param()

# def digits_sum(n, event=True):
#     s = 0
#     while n > 0:
#         num = n % 10
#         if event and num % 2 == 0:
#             s += num
#         if not event and num % 2 != 0:
#             s += num
#         n //= 10
#     return s


# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
#
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, event=False))
# print(digits_sum(38271, event=False))
# print(digits_sum(123456789, event=False))

# def display_info(name, age):
#     print("Name: ", name, "\nAge: ", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
#
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = "Hello"  #3,  3.2, True, False
# b = "Hello"  #3,  3.2, True, False
# print(id(a))
# print(id(b))
#
# print(a == b)
# print(a is b)

# s = "Hello"
# print(s, id(s))
# s += "World"
# print(s, id(s))
#
# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))

# s = "Hello"
# print(s, id(s))
# s += s[1: -1]
# print(s, id(s))

# def add_number(n):
#     print("Внутри функции: ", n, id(n))
#     n = n + [4]
#     print("Измененное значение: ", n, id(n))
#
#
# x = [1, 2, 3]
# print("до функции: ", x, id(x))
# add_number(x)
# print("после функции: ", x, id(x))


# Кортеж
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst)
# print(tpl)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)
# print(a, type(a))
# c = 1, 2, 3, 4, 5
# print(type(c))
# b = tuple(c)
# print(b, type(b))
#
# t = (1,)
# print(type(t))

# a = (1, 2, 3, 4, 5)
# print(a)
# print(a[3])
# print(a[1:3])
# a[3] = 55
# print(a)

# s = [int(input("-> ")) for i in range(3)]
# print(s)
# s = tuple(int(input("-> ")) for i in range(3))
# print(s)

# from random import randint
# s = [randint(1, 20) for i in range(10)]
# print(tuple(s))
# s = tuple(randint(1, 20) for i in range(5))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l', 4))
#
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("такого нет")

# for i in t3:
#     print(i*2, end="")
# print("\n", t3)

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             start = tpl.index(el)
#             second = tpl.index(el, tpl.index(el) + 1)
#             return tpl[start: second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1,2,3),8))
# print(slicer((1,8,3,4,8,8,9,2),8))
# print(slicer((1,2,8,5,1,2,9),8))

from random import randint

# a = [randint(0, 5) for i in range(10)]
# print(tuple(a))
# b = [randint(-5, 0) for i in range(10)]
# print(tuple(b))
# c = a + b
# print(tuple(c))
# d = c.count(1)
# print(d)


# def tuple_func(start, end):
#     return tuple(randint(start, end) for _ in range(10))
#
#
# tuple_1 = tuple_func(0, 5)
# tuple_2 = tuple_func(-5, 0)
# tuple_3 = tuple_1 + tuple_2
# count_0 = tuple_3.count(0)
#
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print('Count 0:', count_0)

# t = (10, "Hello", [1, 2, 3], (4, 5, 6), ["hello", "world"])
# print(t, id(t))
# t[-1][0] = 'new'
# print(t, id(t))
#
# print(t[1][2:5], id(t))
# t[4].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t     #распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age,is_married
#
#
# user = get_user()
# print(user)
# name1, age1, is_married1 = user
# print(user[0])
# print(user[1])
# print(user[2])
# print(name1, age1, is_married1)
#
# name2, age2, is_married2 = get_user()
# print(name2, age2, is_married2)\

# t = (1, 2, 3)
# # del t
# # print(t)
# print(t)
# t = list(t)
# print(t)
# t.append(4)
# print(t)
# t = tuple(t)
# print(t)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана: ", countryName, "Население= ",countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород: ", cityName, "Население = ", cityPopulation)


# Множество

# s = {"banana", "apple", "orange", "apple"}
# print(type(s))
# print(len(s))
# print(s)
# b = 'Hello', 'Hi'
# a = set(b)
# print(type(a))
# print(a)

# s = {x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# # num = {i for i in numbers if i % 2 == 0}
# num = list(set(numbers))
# print(num)

# to_set = ('я обычная строка')
# print(to_set)
# to_set = set(to_set)
# print(to_set, len(to_set))


# def to_set(s):
#     print(s)
#     return set(s), len(set(s))
#
#
# s_ = 'я обычная строка'
# lst = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
# print(to_set(s_))
# print(to_set(lst))


# t = {'red', 'green', 'blue'}
# # print('green' not in t)
#
# # pr = {2, 5, 3, 7, 11}
# for i in t:
#     print(i, end=" ")


# s = ['ad_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in s if 'a' not in i}   #условия если
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s}   #два условия если и иначе
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c'} #три условия если или если иначе
# print(a)

# a = {0, 1, 2, 3}
# a.add(4)  #добавление элемента
# print(a)
# if 1 in a:
#     a.remove(1)  #удаление элемента
# print(a)
# a.discard(3) #удаление элемента , без генерации исключения
# print(a)
# a.pop() # удаление первого элемента, генерация исключения будет пр попытке удаления из пустого множества
# print(a)
# a.clear()
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a.union(b)
# c = a | b
# a |= b
# c = a & b
# a &= b
# c = a - b
# a -= b
# c = a ^ b
# a ^= b
# c = a <= b
# print(c)
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}

# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print("Min = ", min(s))
# print("Max = ", max(s))

# str1 = "Hello"
# str2 = "How are you"
# s = set(str1) & set(str2)
# print(s)
# for i in s:
#     print(i, end=" ")

# str1 = "Python"
# str2 = "Programming language"
# s = set(str1) - set(str2)
# print(s)
# for i in s:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Женя", "Илья"}
#
# only_one_hobby = drawing ^ music
# print("Только одно хобби: ", only_one_hobby)
# beth_hobby = drawing & music
# print("посещает два кружка: ", beth_hobby)
# drawing = drawing - beth_hobby
# print(drawing)

# frozenset

# s = frozenset({1, 2, 3, 4, 6})
# print(s)
# print(type(s))

# Словарь (dict)

# s = [1, 2]
# d = {'one': 1, 'two': 2, 'ten': 10, 'one': 11}
# print(s[0], s[1])
# print(d['one'], d['two'])
# print(d)

# d = {}
# d = {"one": "Один", "two": "Два"}
# print(d)
# print(type(d))
#
# d["one"] = "Один"
# d["two"] = "Два"
# print(d)

# d1 = dict()
# d1 = dict(one=1, two="Два")
# print(d1)

# d = {0: "text1", "one": 45, (1, 2, 3): 'кортеж', 42: [42, 2, 5], True: 1}
# print(d)
# d["one"] = 100
# d[42][1] = 100
# print(d[0], d["one"], d[42])

# d = {a: a**2 for a in range(2, 7)}
# print(d)

# d = [1, 2, 3]
# print(d)
# print(set(d))
# print(tuple(d))

# user = [
#     ['igor@gmail.com', 'Igor'],
#     ['irina@gmail.com', 'Irina'],
#     ['anna@gmail.com', 'Anna'],
# ]
#
# print(user)
# d_user = dict(user)
# print(d_user)
# print()

# users = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna'),
# )
#
# print(users)
# d_users = dict(users)
# print(d_users)
#
# # print('igor@gmail.com' in d_users)
#
# for key in d_users:
#     print(key, "->", d_users[key])


# str1 = input("Введите первую строку: ")
# str2 = input("Введите вторую строку: ")
# s = set(str1) - set(str2)
# print(s)
# for i in s:
#     print(i, end=" ")


# letter = 'аоуэыяёюеиaeiouy'
# str1 = input("Введите строку: ")
# count = 0
#
# for i in str1:
#     for b in letter:
#         if b in i:
#             count += 1
#
# print("Количество гласных букв: ", count)

# d = {'one': 1, 'two': 2, 'three': 3}
# key = 'two1'


# if key in d:
#     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# print(d)


# a = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# mult = 1
# for key in a:
#     mult *= a[key]
# print(mult)


# a = dict()
# a[1] = input("->")
# a[2] = input("->")
# a[3] = input("->")
# a[4] = input("->")
# a = {i: input("->")for i in range(1, 5)}
# print(a)

# dislike = int(input("Исключить: "))
# del d[dislike]
# print(a)

# d = {'one': 1, 'two': 2, 'three': 3}
# print(len(d))

# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium 63220", 8, 2100],
#     "5": ["Core i5-3450", 5, 6400],
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " шт, по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("Введите №: ")
#     if n != "0":
#         m = int(input("Количество штук: "))
#         goods[n][1] = m
#     else:
#         break
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " шт, по ", goods[i][2], "руб", sep="")

# Методы словарей

# d = {'one': 1, 'two': 2, 'three': 3}
# print(d["two"])
# value = d.get("two") #получаем элемееи из словаря
# value1 = d.get("two1", "Ключа нет")
# print(value)
# print(value1)
#
# print(d.keys())  #список ключей
# print(d.items())   #список кортежа из ключа и значения
# print(d.values())   #список значений
#
# for i in d.items():
#    print(i)
#
# for key, value in d.items():   #распаковка кортежа
#     print(key, "=>", value)
#
# d.clear()   # очистка словаря
# d2 = d
# d2 = d.copy()  # копия словаря
# print("D = ", d)
# print("D2 = ", d2)
#
# d["four"] = 4
# d2["five"] = 5
# print("D = ", d)
# print("D2 = ", d2)
# item = d.pop('two') # удаляет элемент по ключу, возвращает удаляемое значение(не ключ)
# item = d.pop('two1', "Ключа нет")
# item = d.setdefault("three")
# item = d.setdefault("four", 4) # добавляет ключ и значение по умолчанию если ключа нет
# print(item)

# item = d.popitem() #удаляет последнюю и может произвольную пару ключ и значение и их возвращает в виде кортежа
# print(item)
# d.update({'four': 4, 'five': 5})
# d.update([('four', 4), ('three', 5)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x.copy()
# z.update(y)
# z = x | y  # объединение словарей с сохранением в новый словарь
# z = {i: d[i] for d in [x,y] for i in d} # объединение словарей с сохранением в новый словарь
# print(z)

# sp = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_sp = {}
# new_sp['name'] = sp.pop('name')
# new_sp['salary'] = sp.pop('salary')
# print(sp)
# print(new_sp)

# sp = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# sp['location'] = sp.pop('city')
# print(sp)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     },
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ":", a[x][y], sep="")

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1895},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }

# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Введите новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# new_d = {k: v for k, v in d.items() if v < 3}
# print(new_d)

# s = "Hello"
# d = {i: i * 3 for i in s}
# print(d)

# lt = [1, 2, 3, 4]
# value = int(input("->"))
# d = {i: input("->") for i in lt}
# d = {i: value for i in lt}
# print(d)

# Преобразование типов

# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# value = list(d)
# value = list(d.values())
# value = list(d.items())
# print(value)

# a = ["one", 1, 2 ,3, 'two', 10, 20, "three", 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)
# d = dict(zip([1,2,3], ['one', 'two', 'three']))
# print(d)
# d = list(zip([1,2,3], ('one', 'two', 'three')))
# print(d)

# a = [1, 2, 3]
# print(list(zip(a)))

# print(list(zip(range(5), range(84, 100))))

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# c = [4.0, 5.4, 6.7]
# print(list(zip(a,b,c)))


# dict_one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# dict_two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2)in zip(dict_one.items(), dict_two.items()):
#     print(k1, v1)
#     print(k2, v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # print(dict(pairs))
# a, b = zip(*pairs)
# print(a)
# print(b)

# letters = ['b', 'a', 'd', 'c']
# numbers = [3, 1, 2, 4]
# data = list(zip(letters, numbers))
# print(data)
# data.sort()
# print(data)
# data1 = list(zip(numbers, letters))
# data1.sort()
# print(data1)
# data2 = dict(data1)
# print(data2)
# data3 = sorted(data2.items())
# print(data3)

# one = {'apple': 0.4, 'orange': 0.35, 'pepper': 0.5}
# two = {'pepper': 0.2, 'onion': 0.55}
#
# print({**two, **one})  #Распаковка словаря
#
# for k, v in {**two, **one}.items():
#     print(k, "->", v)

# data = [2, 5, 3, 4, 1, 5]
# for i in data:
#     print(i, end=" ")
# print()
# for i in range(6):
#     print(i, end=" ")
# print()
#
# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1

# colors = ['red', 'green', 'blue']
# for num, val in enumerate(colors, 1):
#     print(num, ") ", val, sep="")

# n = {i: i+1 for i in range(10, 18)}
# print(n)
#
# for i, (j, v) in enumerate(n.items(), 100):
#     print(i, ": ", j, "->", v, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(2, 3, 4, 5, 1))
# print(func(2, 4, 7))
# print(func())


# def to_dict(*lst):
#     n = {i: i for i in lst}
#     return n
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def lst(*args):
#     res = []
#     sr = sum(args) / len(args)
#     print(sr)
#
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(lst(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(lst(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))

# def print_scores(student, *scores):
#     print("Student Name: ", student)
#     for score in scores:
#         print(score)
#
#
# print_scores("Джонатан", 100, 95, 88, 92, 99)
# print_scores("Роман", 87, 22, 49)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(d="python"))

# def db(**data):
#     my_dict.update(data)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=23, weight=61, eyes_color='grey')
# print(my_dict)

# def func(aa, *args, d=0, **kwargs):
#     return aa, args, d, kwargs
#
#
# print(func("one", 5, 9, 7, 8, 1, d=6, a=1, b=2, c=3))

# Области Видимости (4 видимости)

# name = "Tom" #Глобальная переменная
# surname = None
#
# def hi():
#     global name, surname
#     name = "Sam" #Локальная переменная
#     surname = "Johnson" #Локальная переменная
#     print("Hello", name, surname)
#
#
#
# def by():
#     print("Godd bye", name, surname)
#
#
#
# print(name)
# hi()
# by()
# print(name)

# i = 5
# arg = 5
#
#
# def func(arg):
#     print(arg)
#
#
# i = 6
# arg = 6
# func(arg)

# x = 7
#
#
# def add_five(a):
#     # x = 2
#
#     def add_two():
#         return a + x
#
#     return add_two()
#
#
# print(add_five(3))

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# min = [5, 6, 8, 9, 7]
# print(min(min))

# Вложенные функции

# def outer_func(who):
#     def inner_func():
#         print("Hello, ", who)
#
#     inner_func()
#
#
# outer_func('World!')

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("a + b = ", a + b)
#
#     print("a = ", a)
#     fun2(4)
#
#
# fun1()

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal: ", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# z = x + t  # 25+30=55
# print(z)


# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x=', x)
#
#     fn2()
#     print('fn1.x=', x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a,b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add2(10))
#
# print(outer(7)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "1"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def func1():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return func1
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func("Cочи")
# res2()
# res2()
# res1()


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 86,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
# A = make_classifier(90, 100)
# B = make_classifier(70, 90)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
#
# print("A = ", A(students))
# print("B = ", B(students))
# print("C = ", C(students))
# print("D = ", D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())

# Анонимные функции Lambda

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
# func = lambda x, y: x + y
#
# print(func(1, 2))
# print(func('a', 'b'))


# либо через def

# def summa(x, y):
#     return x + y
#
#
# print(summa(1, 2))
# print(summa('a', 'b'))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# s = lambda a=1, b=2, c=3: a + b + c
#
# print(s())
# print(s(10, 20, 30))
#
# s = lambda *args: args
# print(s(1, 2, 3, 4))

# f = (lambda x: x*2,
#      lambda x: x*3,
#      lambda x: x*4)
#
# for i in f:
#     print(i('abc_'))


# def inc1(n):
#     def add_two(x):
#         return x + n
#
#     return add_two
#
#
# def inc(n):
#     return lambda x: x + n

# inc = (lambda n: (lambda x: x + n))
#
# print(inc(42)(1))
# print(inc(42)(3))
# f = inc(42)
# print(f(1))
# print(f(3))

# sum3 = (lambda x: lambda y: lambda z: x + y + z)
# print(sum3(2)(4)(6))

# def func(i):
#     return i[1]
#
# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort()
# print(lst)
# lst.sort(key = lambda i: i[1])
# print(lst)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
#     ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[3](15, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: x + 3, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[4]()

# print((lambda a, b: a if a > b else b)(15, 23))

# print((lambda a, b, c: a if a < b and a < c else b if b < c else c)(9, 8, 5))
# print((lambda a, b, c: min((a, b, c)))(10, -1, 2))

# map(func, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [1, 8, 12, -5, -10]
#
# lst2 = list(map(mult, lst))

# print(list(map(lambda t: t*2), [1, 8, 12, -5, -10])))

# areas = [3.45154, 5.2366, 2.66551]
#
# print(list(map(round, areas, range(1,7))))
# print(round(3.4531, 2))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x,y: (x, y), st, num)))
# print(dict(map(lambda x,y: (x, y), st, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))

# b = [66, 90, 68, 59, 76, 60, 80, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# lst = [random.randint(1, 30) for _ in range(10)]
# или
# numbers = []
# for i in range(10):
#     numbers.append(randint(-10, 100))
# print(numbers)
#
# res = list(filter(lambda s: 9 <s<21, numbers))
# print('[10; 20] =', res)

# m = list(map(lambda x: x **2, filter(lambda x: x % 2, range(10))))
# print(m)
# m1 = [x **2 for x in range(10) if x % 2]
# print(m1)

# Декоратор


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_hello'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func): # декорирующая функция
#     def func_wrapper():
#         print('************ ')
#         func()
#         print('______________________')
#
#     return func_wrapper
#
#
# @my_decorator  #Добавили декоратор
# def func_test(): #Декорируемая функция( которую декорируем)
#     print("Hello, I am func 'func_test'")
#
# @my_decorator
# def bye():
#     print("Hello, I am func, bye")
#
# func_test()
# print()
# bye()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "<b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "<i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         print("1)", args[1])
#         print("kw)", kwargs['study'])
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают ", study, "\n")
#
#
# print_full_name("Ирина", "Елизовета", "Елена", study="JavaScript")
# print_full_name("Мария", "Юлия", "Игорь")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(n1):
#     def mult(fn):
#         def wrap(n2):
#             return n1 * fn(n2)
#
#         return wrap
#     return mult
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорретный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорретный тип данных именовоного параметра")
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Dog"))
# print(typed_fn2("Hello ", "world ", "!"))
# # print(typed_fn2(3, 4, 5))
# print(typed_fn3("Hello ", "world ", z=5))

# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world('Hi!')
# hello_world2('world!')


# Строки

# print(int("18"))
# print(int(18.5))
# print(int("18a5"))

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))

# print(bin(18)) #0b10010
# print(oct(18)) #0o22
# print(hex(18)) #0x12

# print(0b10010)
# print(0o22)
# print(0x12)
# print(0xFF)

#  #FF0000 #rgb(255, 0, 0)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
#
# print(e in "I am learn Python")
# print(e[5::-1])
# print(e[3])
# e = e[0:3] + "t" +e[4:]
# print(e)

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1)

# str2 = str1[:9] + "P" +str1[10:30] + "P" + str1[31:38]+ "P" + str1[39:]
# print(str2)

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 +=c_new
#         else:
#             s2 += s[i]
#         i +=1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = changeCharToStr(str1, "и", "P")
# print(str1)
# print(str2)

# print(u"Привет")
# print("Привет")

# print(r'C:\Users\Вениамин\Desktop\Пайтон')
# print(r'C:\Users\Вениамин\Desktop\Пайтон\\')
# print(r'C:\Users\Вениамин\Desktop\Пайтон\\')
# print(r'C:\Users\Вениамин\Desktop\Пайтон\\'[:-1])
# print(r'C:\Users\Вениамин\Desktop\Пайтон' + "\\")

# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd')
# print(b'\xff\xfe\xfd'[1])

# name = "Дмитрий"
# age = 25
# print("меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("меня зовут " + name + ". Мне " + str(age) + " лет.")
#
# print(f"меня зовут {name}. Мне {age} лет.")

# from math import pi

# print(f"Значение числа pi: {round(pi, 2)}")
# print(f"Значение числа pi: {pi:.2f}")

# x = 10
# y = 5
# print(f"{x = }\n{y = }")
# print(f"{x} * {y} / 2 = {x*y/2}")

# a = 74
# print(f"{{{{{a}}}}}")

# dir_name = "my_doc"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name +"\\" + file_name)

# s = """<div>
#     <a href="#">content</a>
# </div>"""
# s1 = '''<div>
#     <a href="#">content</a>
# </div>'''
# print(s)
# print(s1)
#
# '''<div>
#     <a href="#">content</a>
# </div>'''
# "Python"


# def square(n):
#     """Принимает число n, и возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# import math as m
#
#
# def cylinder(r, h):
#     """
#     Функция вычисляет площадь цилиндра.
#
#     Функция вычисляет площадь цилиндра, на основании заданной высоты и радуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * m.pi * r * (r+h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))
# print(ord('#')) #35
# print(ord('к')) #1082

# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# my_str = 'Test string for mes'
# arr = [ord(x) for x in my_str]
# print("ASCII коды: ", arr)
# # s = sum(arr)//len(arr)
# # arr.insert(0, s)
# arr = [sum(arr)//len(arr)] + arr
# print("Среднее арифметическое: ", arr)
# arr += [x for x in [ord(x) for x in (input("->" + " ")[:6])] if x not in arr]
# #arr += [ord(x) for x in (input("->" + " ")[:6]) if x not in arr]
# print("Среднее арифметическое: ", arr)
#
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов: ", arr.count(arr[-1]) -1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(101))
# print(chr(84))
# print(chr(1036))

# a = 97
# b = 122
#
# print(*(chr(x) for x in range(a, b+1)) if a < b else (chr(x) for x in range(b, a+1)))
# z = [chr(x) for x in range(min(a, b), max(a, b) + 1)]
# print(*z)








