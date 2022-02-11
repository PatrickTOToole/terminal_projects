from math import floor
from classes import Vector2
from classes import Display

class Line:
    def __init__(self, length, direction, pos, display):
        self.length = length
        self.direction = direction
        self.pos = pos
        self.display = display
    def draw(self):
        vect = self.direction.to_unit() 
        for i in range(self.length):
            point_x = floor(self.pos.x + i * vect.x)
            point_y = floor(self.pos.y + i * vect.y)
            self.display.set_point(point_x, point_y, "@")
            self.display.add_to_cache(point_x, point_y)
    def set_direction(self, direction):
        self.direction = direction
    def set_pos(self, pos):
        self.pos = pos
    def move(self, vector2):
        self.set_pos(self.pos + vector2)
