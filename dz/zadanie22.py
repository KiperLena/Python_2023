from math import pi


class Sphere:

    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def get_volume(self):
        return 4 / 3 * (pi * self.r ** 3)

    def get_square(self):
        return 4 * pi * (self.r ** 2)

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if ((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2) <= self.r ** 2:
            return True
        else:
            return False


p1 = Sphere(0, 0, 0, 0.6)
print("get_radius: ", p1.get_radius())
print("get_volume: ", p1.get_volume())
print("get_square: ", p1.get_square())
print("get_center: ", p1.get_center())
print(p1.is_point_inside(0, -1.5, 0))
p1.set_radius(1.6)
print("set_radius(1.6):", p1.get_radius())
print(p1.is_point_inside(0, -1.5, 0))
