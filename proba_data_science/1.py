from matplotlib import pyplot as plt
# ПРИМЕР 1 линейный график
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gbp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#
# plt.plot(years, gbp, color='green', marker='o', linestyle='solid')
#
# plt.title("Номинальный ВВП")
# plt.ylabel("Млрд $")
# plt.show()

# ПРИМЕР 2 столбчатый график
# movies = ["Энни Холл", "Бен -Гур", "Касабланка", "Ганди", "Вестсайдская история"]
# num_oscar = [5, 11, 3, 8, 10]
#
# plt.bar(range(len(movies)), num_oscar)
# plt.title("Мои любимые фильмы") #заголовок
# plt.ylabel("Количество наград") #метка на оси y
# plt.xticks(range(len(movies)), movies)
# plt.show() #Вывод на экран


# ПРИМЕР 3 столбчатый график

from collections import Counter

#
# grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
#
# plt.bar([x + 5 for x in histogram.keys()], list(histogram.values()), 10, color="green")
# plt.axis([-5, 105, 0, 5]) #ось х от -5 до 105, ось у от 0 до 5
#
# plt.xticks([10 * i for i in range(11)]) #метки по оси х 0, 10..100
# plt.xlabel("Дециль")
# plt.ylabel("Число студентов")
# plt.title("Распределение оценок за экзамент №1")
# plt.show()

# ПРИМЕР 4 столбчатый график

# mentions = [500, 505]
# years = [2017, 2018]
#
# plt.bar(years, mentions, 0.8)
# plt.xticks(years)
# plt.ylabel("Число раз, когда я слышал, как упоминали науку о данных")
#
# plt.ticklabel_format(useOffset=False)
#
# plt.axis([2016.5, 2018.5, 499, 506])
# plt.title("Посмотрите, какой 'огромный' прирост!")
# plt.show()

# ПРИМЕР 5 линейные графики

# variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
# bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
#
# total_error = [x + y for x, y in zip(variance, bias_squared)]
# xs = [i for i, _ in enumerate(variance)]
#
# plt.plot(xs, variance, 'g-', label='дисперсия')
# plt.plot(xs, bias_squared, 'r-.', label='смещение^2')
# plt.plot(xs, total_error, 'b:', label='суммарная ошибка')
#
# plt.legend(loc=9)
# plt.xlabel("Сложность модели")
# plt.title("Компромисс между смещением и дисперсией")
# plt.show()

# ПРИМЕР 6 диаграммы рассеяния

# friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutes = [175, 170, 205, 120, 220, 123, 105, 145, 190]
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#
# plt.scatter(friends, minutes, color='red')
#
# for labels, friends_count, minute_count in zip(labels, friends, minutes):
#     plt.annotate(labels,
#                  xy=(friends_count, minute_count),
#                  xytext=(5, -5),
#                  textcoords='offset points',
#                  color='blue')
#
# plt.title("Число минут против числа друзей")
# plt.xlabel("Число друзей")
# plt.ylabel("Число минут. проводимых на сайте ежедневно")
# plt.show()

# ПРИМЕР 7 диаграммы рассеяния

# test_1_grades = [99, 90, 85, 97, 80]
# test_2_grades = [100, 85, 60, 90, 70]
#
# plt.scatter(test_1_grades, test_2_grades)
# plt.title("Оси сопоставимы")
# plt.xlabel("Оценки за экзамен 1")
# plt.ylabel("Оценки за экзамен 2")
# plt.axis("equal")
# plt.show()


# ПРИМЕР 8 статистика

# num_friends = [100, 49, 41, 40, 25, 10, 100, 49, 41, 40, 25, 10, 2, 50, 55, 33, 21, 21, 21, 20, 98, 99, 98, 100]
#
# friend_count = Counter(num_friends)
# xs = range(101) #максимум равен 101
# ys = [friend_count[x] for x in xs] #высота - число друзей
#
# plt.bar(xs, ys)
# plt.axis([0, 101, 0, 25])
# plt.xlabel("Число друзей")
# plt.ylabel("Число людей")
# # plt.show()
#
# num_point = len(num_friends) #количество точек
# largest_value = max(num_friends)
# smallest_value = min(num_friends)
# print(largest_value)
# print(smallest_value)
#
# sorted_values = sorted(num_friends)
# smallest_value = sorted_values[0]
# second_smallest_value = sorted_values[1]
# second_largest_value = sorted_values[-2]
#
# print(sorted_values)
# print(smallest_value)
# print(second_smallest_value)
# print(second_largest_value)