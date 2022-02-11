from math import sqrt

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)
    @staticmethod
    def up():
        return Vector2(0,-1)
    @staticmethod
    def down():
        return Vector2(0,1)
    @staticmethod
    def left():
        return Vector2(-1, 0)
    @staticmethod
    def right():
        return Vector2(1, 0)
    def to_unit(self):
        mag = sqrt((self.x)**2 + (self.y)**2)
        x = self.x / mag
        y = self.y / mag
        return Vector2(x, y)
    def smult(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector2(x, y)
    def sdiv(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        return Vector2(x, y)
