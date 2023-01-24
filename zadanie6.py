def place_rect(a, b):
    print("Площадь прямоугольника = ", a * b)


x = int(input(" Введите значение одной стороны прямоугольника:"))
y = int(input(" Введите значение второй стороны прямоугольника:"))
place_rect(x, y)

print()


def place_triangle(a, b):
    print("Площадь треугольника = ", 0.5 * a * b)


x = int(input(" Введите значение основания треугольника:"))
y = int(input(" Введите значение высоты треугольника:"))
place_triangle(x, y)

print()


def place_circle(a):
    pi = 3.14
    print("Площадь круга = ", pi * a**2)


x = int(input(" Введите значение радиуса круга:"))
place_circle(x)