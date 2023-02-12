# Задача №1
from random import randint


# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# a = [randint(1, 100) for i in range(10)]
# a.sort()
# print(a)
# n = int(input("Введите число: "))
# if seq_search(a, n):
#     print(f"Число {n} в списке присутсвует")
# else:
#     print(f"Число {n} в списке отсутствует")

# Задача №2
# n = int(input("Введите строку которую хотите удалить: "))
#
# f = open('dz19.txt', mode='w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open('dz19.txt', mode='r')
# list = f.readlines()
# print(list)
# del list[n]
# print(list)
# f.close()
#
# f = open('dz19.txt', mode='w')
# for i in list:
#     f.write(i)
# f.close()


# Задача №3


# def quick_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1) // 2]
#         low = [i for i in a if i < x]
#         eq = [i for i in a if i == x]
#         hi = [i for i in a if i > x]
#         a = quick_sort(low) + eq + quick_sort(hi)
#     return a
#
#
# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# a1 = [5, 9, 6, 7]
# a2 = [3, 11, 8]
# a3 = [2, 4]
# a4 = [10, 1, 12]
# a = a1 + a2 + a3 + a4
# print(a)
# m = int(input("1 - сортировка по убыванию \n2 - сортировка по возрастанию\n Введите сортировку:\n -> "))
#
# if m == 1:
#     a = quick_sort(a)
#     a = a[::-1]
#
# else:
#     a = quick_sort(a)
# print(a)
# n = int(input("Введите число: "))
# if seq_search(a, n):
#     print(f"Значение {n} найдено")
# else:
#     print(f"Значение {n} не найдено")
