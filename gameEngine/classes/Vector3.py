from math import sqrt

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3(x, y, z)
    @staticmethod
    def up():
        return Vector3(0, -1, 0)
    @staticmethod
    def down():
        return Vector3(0, 1, 0)
    def to_unit(self):
        mag = sqrt((self.x)**2 + (self.y)**2 + (self.z)**2)
        x = self.x / mag
        y = self.y / mag
        z = self.z / mag
        return Vector3(x, y, z)
    def smult(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        return Vector3(x, y, z)
    def sdiv(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        z = self.z / scalar
        return Vector3(x, y, z)
    def to2D():
        return Vector2(x, y)
    def to2DProj(plane):
        
