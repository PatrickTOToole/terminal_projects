from gameEngine.classes import *

class Player:
    def __init__(self, obj, screen_bounds):
        self.obj = obj
        self.direction = Vector2(0, 0)
        self.screen_bounds = screen_bounds
    def set_direction(self, new_dir):
        self.direction = new_dir
    def update(self):
        bounds = self.obj.display.get_dims()
        pos = self.obj.get_pos()
        direction = self.direction
        screen_bounds = self.screen_bounds
        if pos.y >= screen_bounds.y and direction.equals(Vector2.up()):
            self.obj.move(direction)
        elif pos.y <= screen_bounds.x and direction.equals(Vector2.down()):
            self.obj.move(direction)
        elif screen_bounds.x <= pos.y <= screen_bounds.y:
            self.obj.move(direction)
