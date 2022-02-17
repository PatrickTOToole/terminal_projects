from gameEngine.classes.Dot import Dot


class Ball:
    def __init__(self, pos, direction, display):
        self.dot = Dot(pos, display)
        self.direction = direction
        self.pos = pos
    def move(self):
        self.dot.move(self.direction.smult(0.5))
        self.pos = self.dot.pos
    def draw(self):
        self.dot.draw()
    def set_dir(self, direction):
        self.direction = direction
    def set_pos(self, pos):
        self.pos = pos
        self.dot.pos = pos
