from gameEngine.classes.Vector2 import Vector2
from os import system


class Display:
    def __init__(self, dim_x, dim_y):
        display = []
        for i in range(dim_x):
            display.append([])
            for j in range(dim_y):
                display[i].append(" ")
        self.display = display
        self.objs = []
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.cache = []
    def set_point(self, x, y, val):
        x = int(x)
        y = int(y)
        if x <= len(self.display) - 1 and x >= 0 and y >= 0 and y <= len(self.display[0]) - 1:
            if self.cache.__contains__([x,y]):
                self.cache.remove([x,y])
            self.display[x][y] = val
    def update(self):
        self.draw()
        system('clear')
        for j in range(self.dim_y):
            row = ""
            for i in range(self.dim_x):
                row = row + self.display[i][j]
            print(row)
        for elt in self.cache:
            x = int(elt[0])
            y = int(elt[1])
            self.display[x][y] = " "
        self.cache = []
    def draw(self):
        for obj in self.objs:
            obj.draw()
    def add_to_cache(self, x, y):
        if not self.cache.__contains__([x,y]):
            if x <= len(self.display) - 1 and x >= 0 and y >= 0 and y <= len(self.display[0]) - 1:
                self.cache.append([x,y])
    def get_dims(self):
        return [len(self.display) - 1, len(self.display[0]) - 1]
    def add_obj(self, obj):
        self.objs.append(obj)
        
        
