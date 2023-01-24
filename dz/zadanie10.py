# задача№1
# Глобальная

# def fn(a, b, c):
#     s = 2 * (a * b + b * c + a * c)
#     print(s)
#
#     def fn2():
#         s2 = a * b
#     fn2()
#
#
# fn(2, 4, 6)


# Локальная
# a = 2
# b = 4
# c = 6
#
#
# def fn():
#     global a, b, c
#     a, b, c = 5, 8, 2
#     s = 2 * (a * b + b * c + a * c)
#     print(s)
#
#     def fn2():
#         s2 = a * b
#     fn2()
#
#
# fn()

# Нелокальная

# def fn():
#     a, b, c = 5, 8, 2
#
#     def fn2():
#         nonlocal a, b, c
#         a, b, c = 1, 6, 8
#         s = 2 * (a * b + b * c + a * c)
#         s2 = a * b
#         print(s)
#
#     fn2()
#
#
# fn()
