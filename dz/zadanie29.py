class Checking:
    @staticmethod
    def verify_type(value):
        if not isinstance(value, int):
            raise TypeError("Значение стороны должно быть целым числом")

    @staticmethod
    def verify_min(value):
        if value < 0:
            raise ValueError("Значение должно быть больше нуля")

    @staticmethod
    def verify_nul(value):
        if value == 0:
            raise ValueError("Значение не должно быть равно нулю")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_type(value)
        self.verify_min(value)
        self.verify_nul(value)
        instance.__dict__[self.name] = value


class Triangle:
    x = Checking()
    y = Checking()
    z = Checking()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def info(self):
        if self.x + self.y < self.z:
            print(f"Треугольник со сторонами ({self.x}, {self.y}, {self.z}) не существует")
        else:
            print(f"Треугольник со сторонами ({self.x}, {self.y}, {self.z}) существует")


tr1 = Triangle(2, 7, 6)
tr1.info()
tr2 = Triangle(5, 2, 8)
tr2.info()
tr3 = Triangle(7, 3, 6)
tr3.info()










