from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calc_perimeter(self):
        pass

    @abstractmethod
    def calc_square(self):
        pass

    @abstractmethod
    def info(self):
        s = self.calc_square()
        p = self.calc_perimeter()
        print(f"Площадь: {s}", end="")
        print(f"\nПериметр: {p}")

    @abstractmethod
    def painting(self):
        pass


class Square(Shape):

    def __init__(self, a, color):
        self.a = a
        self.color = color

    def calc_perimeter(self):
        return self.a * 4

    def calc_square(self):
        return self.a ** 2

    def info(self):
        s = self.calc_square()
        p = self.calc_perimeter()
        print("=" * 3, "Квадрат", "=" * 3)
        print(f"Сторона: {self.a}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {s}", end="")
        print(f"\nПериметр: {p}")

    def painting(self):
        for r in range(self.a):
            print("*" * self.a)


class Rectangle(Shape):

    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color

    def calc_perimeter(self):
        return (self.a + self.b) * 2

    def calc_square(self):
        return self.a * self.b

    def info(self):
        s = self.calc_square()
        p = self.calc_perimeter()
        print("=" * 3, "Прямоугольник", "=" * 3)
        print(f"Длина: {self.a}")
        print(f"Ширина: {self.b}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {s}", end="")
        print(f"\nПериметр: {p}")

    def painting(self):
        for r in range(self.a):
            print("*" * self.b)


class Triangle(Shape):
    def __init__(self, a, b, c, color):
        self.a = a
        self.b = b
        self.c = c
        self.color = color

    def calc_perimeter(self):
        return self.a + self.b + self.c

    def calc_square(self):
        h = math.sqrt(self.b ** 2 - ((0.5 * self.a) ** 2))
        return round(0.5 * h * self.a, 2)

    def info(self):
        s = self.calc_square()
        p = self.calc_perimeter()
        print("=" * 3, "Треугольник", "=" * 3)
        print(f"Сторона 1: {self.a}")
        print(f"Сторона 2: {self.b}")
        print(f"Сторона 3: {self.c}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {s}", end="")
        print(f"\nПериметр: {p}")

    def painting(self):
        for i in range(1, self.b * 2, 2):
            print(('*' * i).center(self.b * 2))


obj = [Square(3, "red"), Rectangle(3, 7, "green"), Triangle(11, 6, 6, "yellow")]
for i in obj:
    i.info()
    i.painting()
    print()
