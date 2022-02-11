from time import sleep
from os import system
from math import floor, sqrt
from sys import exit
from pynput import keyboard

LOG_FILE = open("log", "w")
class Logger:
    def __init__(self, file_obj):
        self.file_obj = file_obj
    def log(self, text, end="\n"):
        if type(text) != str:
            text = str(text)
        self.file_obj.write(text + end)

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



class Display:
    def __init__(self, dim_x, dim_y):
        display = []
        for i in range(dim_x):
            display.append([])
            for j in range(dim_y):
                display[i].append(" ")
        self.display = display
        self.objs = []
        self.cache = []
    def set_point(self, x, y, val):
        if x <= len(self.display) - 1 and x >= 0 and y >= 0 and y <= len(self.display[0]) - 1:
            if self.cache.__contains__([x,y]):
                self.cache.remove([x,y])
            self.display[x][y] = val
    def update(self):
        self.draw()
        system('clear')
        for j in range(50):
            row = ""
            for i in range(100):
                row = row + self.display[i][j]
            print(row)
        for elt in self.cache:
            x = elt[0]
            y = elt[1]
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
        
        
class Line:
    def __init__(self, length, vector2, center, display):
        self.length = length
        self.vector = vector2
        self.center = center
        self.display = display
    def draw(self):
        vect = self.vector.to_unit() 
        for i in range(self.length):
            point_x = floor(self.center.x + i * vect.x)
            point_y = floor(self.center.y + i * vect.y)
            self.display.set_point(point_x, point_y, "@")
            self.display.add_to_cache(point_x, point_y)
    def set_vect(self, vector2):
        self.vector = vector2
    def set_center(self, vector2):
        self.center = vector2
    def move(self, vector2):
        new_center = self.center + vector2
        self.set_center(new_center)

            
        
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
            
logger = Logger(LOG_FILE)

class CircleList:
    def __init__(self, in_list):
        self.in_list = in_list
        self.curr = 0
    def nextv(self):
        self.curr = (self.curr + 1) % len(self.in_list)
        return self.in_list[self.curr]
        
try:
    var_dir = Vector2(0, 0)


    def on_press(key):
        global var_dir
        if key == keyboard.Key.esc:
            logger.log("bye")
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if k in ['left', 'up', 'down', 'right']:
            if k == 'left':
                var_dir = Vector2.left()
            if k == 'right':
                var_dir = Vector2.right()
            if k == 'up':
                var_dir = Vector2.up()
            if k == 'down':
                var_dir = Vector2.down()
            # keys of interest
            # self.keys.append(k)  # store it in global-like variable
            #

    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    
    test_display = Display(100, 50)
    test_line = Line(100, Vector2(1,1), Vector2(20,20), test_display)
    ponger = Line(10, Vector2.down(), Vector2(0,0), test_display)
    test_box = Box(10, 6, [20, 20], test_display)
    vect1 = Vector2.up()
    vect2 = Vector2.left()
    vect3 = Vector2.down()
    vect4 = Vector2.right()
    dirs = CircleList([vect1,vect2,vect3,vect4])
    direction = vect1
    test_display.add_obj(test_line)
    test_display.add_obj(test_box)
    test_display.add_obj(ponger)
    for i in range(100):
        #test_display.draw(test_line)
        #test_display.draw(test_box)
        #test_display.draw(ponger)
        test_display.update()
        if i % 10 == 0:
            direction = dirs.nextv()
        test_box.move(var_dir)
        test_line.move(direction)
        test_line.set_vect(direction)
        sleep(0.1)
except KeyboardInterrupt:
    LOG_FILE.close()
    exit(0)
LOG_FILE.close()
