# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a, b = b, a
#или
# c = a
# a = b
# b = c
#или
# c = a
# a = a - a + b
# b = b - b + c
# или
# c = a + b
# a = c - a
# b = c - b
# или
a = a + b
b = a - b
a = a - b
print("a:", a)
print("b:", b)