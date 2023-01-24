#задача №1

# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: ")))]
# print(a)
# num = int(input("Введите число: "))
# print(num)
# b = a.count(num)
# if b >= 1:
#     print("Число присутствует в элементах списка")
# else:
#     print("Такого числа НЕТ в элементах списка")

#задача №2

# import random as r
# mas = [r.randint(1, 100) for i in range(20)]
# print(mas)
# print("Сумма: ", sum(mas))

#задача №3

# import random as r
# mas = [r.randint(1, 40) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

#задача №4

# import random as r
# mas =[[r.randint(0, 5) for i in range(3)], [r.randint(0, 5) for i in range(3)], [r.randint(0, 5) for i in range(3)], [r.randint(0, 5) for i in range(3)]]
# print(mas)
# for row in range(len(mas)):
#     for col in range(len(mas[row])):
#         print(mas[row][col], end="\t\t")
#     print()
# print()

# w = 1
# for row in range(len(mas)):
#     for col in range(len(mas[row])):
#         if mas[row][col] > 0:
#             w *= mas[row][col]
# print("Произведение ненулевых элементов = ", w)
