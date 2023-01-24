#задача 1
a =[int(input("-> ")) for i in range(int(input("Введите длину списка: \nn= ")))]
print(a)
b = []
for i in a:
    if i > 0:
        b.append(i)
        c = max(a)
print(b)
print(c)

#задача 2
# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: \nn= ")))]
# print(a)
# for i in a:
#     k = int(input("Введите индекс: \nk = "))
#     c = int(input("Введите значение: \nc = "))
#     a.insert(k,c)
#     break
# print(a)


# задача 3

# a = list(range(1,11))
# print(a)
# c = []
# for i in a:
#     b = i ** 2
#     c.append(b)
# print(c)
