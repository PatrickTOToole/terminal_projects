
class Dot:
    def __init__(self, pos, display):
        self.pos = pos
        self.display = display
    def draw(self):
        self.display.set_point(self.pos.x, self.pos.y, "&")
        self.display.add_to_cache(self.pos.x, self.pos.y)
    def set_pos(self, vector2):
        self.pos = vector2
    def move(self, vector2):
        self.set_pos(self.pos + vector2)
