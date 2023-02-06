# Задача №1


# Задача №2


def count(lst):
    if len(lst) == 1:
        if lst[0] < 1:
            return 1
        else:
            return 0
    else:
        if lst[0] < 1:
            return 1 + count(lst[1:])
        else:
            return count(lst[1:])


print("n = ", count([-2, 3, 8, -11, -4, 6]))