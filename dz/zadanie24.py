import math


class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_pair_a(self):
        return self.__a

    def set_pair_a(self, a_new):
        self.__a = a_new

    def get_pair_b(self):
        return self.__b

    def set_pair_b(self, b_new):
        self.__b = b_new

    x = property(get_pair_a, set_pair_a)
    y = property(get_pair_b, set_pair_b)

    def sum(self):
        print("Сумма: ", end="")
        print(self.__a + self.__b)

    def mult(self):
        return self.__a * self.__b

    def kv(self):
        return self.__a ** 2 + self.__b ** 2


class RightTriangle(Pair):

    def __init__(self, a, b):
        super().__init__(a, b)

    def hypotenuse(self):
        print("Гипотенуза ABC: ", end="")
        print(math.sqrt(super().kv()))

    def area(self):
        print("Площадь ABC: ", end="")
        print(0.5 * (super().mult()))


    # def info(self):
    #     print(f"Прямоугольный треугольник: {super().__init__(a,b)}")


p2 = RightTriangle(5, 8)
p2.hypotenuse()
# p2.info()
p2.area()
print()
p2.sum()
print("Произведение:", p2.mult())
print()
p2.x = 6.5
p2.y = 11.04
p2.hypotenuse()
p2.x = 10
p2.y = 20
p2.hypotenuse()
p2.sum()
print("Произведение:", p2.mult())
p2.area()