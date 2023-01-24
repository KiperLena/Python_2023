# Задача 1

# def changeCharToStr(str1, c_old, c_new):
#     str2 = ""
#     i = 0
#     while i < len(str1):
#         if (str1[i] == c_old) and (i%2 == 0):
#             str2 +=c_new
#         else:
#             str2 += str1[i]
#         i +=1
#     return str2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = changeCharToStr(str1, "N", "P")
# print("str1 = ", str1)
# print("str2 = ", str2)

# Задача 2

# s = '0123456789'
# print("s = ", s)
# i = int(input("Введите номер позиции: "))
# s2 = s[:i] + s[i+1:]
# print("s2 = ", s2)

# Задача 3
# i = input("Введите символ: ")
#
#
# def str_old(s):
#     s2 = ""
#     print("s = ", s)
#     for x in s:
#         if x not in i:
#             s2 = s2 +x
#     return s2
#
#
# s2 = str_old("012345363738494")
# print("s2 = ", s2)


# Задача 4

# i = int(input("Введите десятичное число: "))
# print(bin(i)[2:])
