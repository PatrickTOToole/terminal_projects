from math import floor

class Text:
    def __init__(self, value, direction, pos, display):
        self.value = value
        self.direction = direction
        self.pos = pos
        self.display = display
    def draw(self):
        vect = self.direction.to_unit() 
        for i in range(len(self.value)):
            point_x = floor(self.pos.x + i * vect.x)
            point_y = floor(self.pos.y + i * vect.y)
            self.display.set_point(point_x, point_y, self.value[i])
            self.display.add_to_cache(point_x, point_y)
    def set_direction(self, direction):
        self.direction = direction
    def set_pos(self, pos):
        self.pos = pos
    def move(self, vector2):
        self.set_pos(self.pos + vector2)
    def set_value(self, value):
        self.value = value
