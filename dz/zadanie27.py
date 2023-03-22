class Point3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.XYZ = [self.x, self.y, self.z]

    def inf_point(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Координаты должны быть типом int")
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Координаты должны быть типом int")
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Координаты должны быть типом int")
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            raise TypeError("Координаты должны быть типом int")
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __getitem__(self, item):
        if 0 <= item < len(self.XYZ):
            return self.XYZ[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым положительным числом")
        self.XYZ[key] = value


p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)
print("Координаты 1-й точки:", p1.inf_point())
print("Координаты 2-й точки:", p2.inf_point())
p3 = p1 + p2
print("Сложение координат: ", "(", p3.inf_point(), ")")
p3 = p1 - p2
print("Вычитание координат: ", "(", p3.inf_point(), ")")
p3 = p1 * p2
print("Умножение координат: ", "(", p3.inf_point(), ")")
p3 = p1 / p2
print("Деление координат: ", "(", p3.inf_point(), ")")
if p1 == p2:
    print("Равенство координат: True")
else:
    print("Равенство координат: False")

print("x = ", p1[0], "    ", "x1 = ", p2[0])
print("y = ", p1[1], "    ", "y1 = ", p2[1])
print("z = ", p1[2], "    ", "z1 = ", p2[2])

p1[0] = 20
print("Запись значения в координату x:", p1[0])
p1[1] = 30
print("Запись значения в координату y:", p1[1])
p1[2] = 40
print("Запись значения в координату z:", p1[2])

p2[0] = 20
p2[1] = 30
p2[2] = 40
print("Запись значения в координату x:", p2[0])
print("Запись значения в координату y:", p2[1])
print("Запись значения в координату z:", p2[2])
