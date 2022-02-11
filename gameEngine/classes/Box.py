from math import floor        
        
class Box:
    def __init__(self, len_x, len_y, center, display):
        self.center = center
        self.display = display
        self.len_x = len_x
        self.len_y = len_y
        self.x = center[0]
        self.y = center[1]
        
        top_x = center[0] - floor(len_x / 2)
        top_y = center[1] - floor(len_y / 2)
        
        bot_x = center[0] + floor(len_x / 2)
        bot_y = center[1] + floor(len_y / 2)
        
        self.top_left = [top_x, top_y]
        self.bot_right = [bot_x, bot_y]
        
    def draw(self):
        xlen = self.bot_right[0] - self.top_left[0]
        ylen = self.bot_right[1] - self.top_left[1] + 1
        xs = self.top_left[0]
        ys = self.top_left[1]
        
        for x in range(xs, xs + xlen):
            self.display.set_point(x, self.top_left[1], "#")
            self.display.set_point(x, self.bot_right[1], "#")
            
            self.display.add_to_cache(x, self.top_left[1])
            self.display.add_to_cache(x, self.bot_right[1])
            
        for y in range(ys, ys + ylen):
            self.display.set_point(self.top_left[0], y, "#")
            self.display.set_point(self.bot_right[0], y, "#")
            
            self.display.add_to_cache(self.top_left[0], y)
            self.display.add_to_cache(self.bot_right[0], y)
    def set_ylen(self, ylen):
        self.ylen = ylen
    def set_xlen(self, xlen):
        self.xlen = xlen
    def set_center(self, center):
        len_x = self.len_x
        len_y = self.len_y
        self.center = center
        
        top_x = center[0] - floor(len_x / 2)
        top_y = center[1] - floor(len_y / 2)
        bot_x = center[0] + floor(len_x / 2)
        bot_y = center[1] + floor(len_y / 2)
        
        self.top_left = [top_x, top_y]
        self.bot_right = [bot_x, bot_y]
        self.x = center[0]
        self.y = center[1]
    def move(self, vect):
        x = vect.x
        y = vect.y
        self.set_center([self.center[0] + x, self.center[1] + y])
            
