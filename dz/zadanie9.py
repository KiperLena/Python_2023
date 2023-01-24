# задача№1
# a = ['red', 'green', 'blue']
# b = ['#FF0000', '#0080000', '#0000FF']
# c = dict(zip(a, b))
# print(c)

# Задача №2

# d = {a: a ** 3 for a in range(1, 11)}
# print(d)

# Задача№3

# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# d = a | b | c
# print(d)

# Задача№4

# worker = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500},
# }
#
# print(worker['emp3'])
# num = input("У кого меняем: ")
# salary = input("Что меняем: ")
# new_salary = int(input("Введите новое значение: "))
# worker[num][salary] = new_salary
#
# for x in worker:
#     print(x)
#     for y in worker[x]:
#         print("\t", y, ":", worker[x][y], sep="")

# Задача№5

# kol = int(input("Количество студентов: "))
# a = [input("Имя студента: ") for i in range(1, kol + 1)]
# b = {i: int(input("Баллы: ")) for i in a}
# print(b)
# sum_sr = 0
# for x in b:
#     sum_sr += b[x]
# sr = round(sum_sr/kol)
# print("Средний балл: ", sr)
# for x in b:
#     if b[x] > sr:
#         print("Студенты с баллом выше среднего: ", x)



# Задача№6
# a = ['color', 'fruit', 'pet']
# b = ['blue', 'apple', 'dog']
# c = {k: v for k, v in zip(a, b)}
# print(c)
