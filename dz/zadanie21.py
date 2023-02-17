
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print(f"Длина прямоугольника: {self.length}\nШирина прямоугольника: {self.width}")


    def calculation(self):
        s = self.length * self.width
        p = 2 * (self.length + self.width)
        d = (self.length ** 2 + self.width ** 2) ** 0.5
        print(f"Площадь прямоугольника: {s}")
        print(f"Периметр прямоугольника: {p}")
        print(f"Гипотенуза прямоугольника: {d}")


    def painting(self):
        for i in range(self.length):
            print("*" * self.width)




p1 = Rectangle(3, 9)
p1.calculation()
p1.painting()

print()

p2 = Rectangle(5, 10)
p2.calculation()
p2.painting()









