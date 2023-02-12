# Задача №1
import re

s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
# r = r'\+?7\ ?\(?\d{3}\)?\ ?\d{3}\-?\ ?\d{2}\-?\ ?\d{2}'


print(re.findall(r, s))

# Задача №2


# def count(lst):
#     if len(lst) == 1:
#         if lst[0] < 1:
#             return 1
#         else:
#             return 0
#     else:
#         if lst[0] < 0:
#             return 1 + count(lst[1:])
#         else:
#             return count(lst[1:])
#
#
# print("n = ", count([-2, 3, 8, -11, -4, 6]))
