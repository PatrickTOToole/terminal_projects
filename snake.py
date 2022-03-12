from math import floor, sin, cos, radians, ceil
from sys import exit
from os import system
from pynput import keyboard

from gameEngine.classes import *

p1_dir = Vector2(0, 0)
display = Display(100, 50, 100)
p1 = Line(10, Vector2.down(), Vector2(0,1), display)

is_exit = False

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
p1_player = Player(p1, Vector2(1,40))
p2_player = Player(p2, Vector2(1,40))

p1_player.set_direction(Vector2(0,0))


def on_press(key):
    global p1_dir
    global is_exit
    if key == keyboard.Key.esc:
        is_exit = True
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k in [ 'up', 'down','left', 'right']:
        if k == 'left':
            p1_dir = Vector2.left()
        if k == 'up':
            p1_dir = Vector2.up()
        if k == 'down':
            p1_dir = Vector2.down()
        if k == 'right':
            p1_dir = Vector2.right()
        # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        #
def on_release(key):
        global p1_dir
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if k in [ 'up', 'down','left','right']:
            if k == 'left':
                p1_dir = Vector2(0,0)
            if k == 'up':
                p1_dir = Vector2(0,0)
            if k == 'down':
                p1_dir = Vector2(0,0)
            if k == 'right':
                p1_dir = Vector2(0,0)


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # start to listen on a separate thread


ball = Ball(Vector2(50,25), Vector2(-1,0), display)
display.add_obj(p1_player.obj)
display.add_obj(ball)
ball_dir = Vector2.left()
screen_bounds = Vector2(1,40)
try:
    while True:
        if is_exit:
            system('clear')
            LOG_FILE.close()
            exit(0)
        ball.move()
        display.update()
        p1_player.move()
        p1_player.update()

        sleep(0.01)
    system('clear')
    banner_arr = ["_","-","‾","-"]
    banner_length = len(banner_arr)
    for i in range(10):
        system('clear')
        banner1 = banner_arr[i % banner_length]
        banner1 += banner_arr[(i + 1) % banner_length]
        banner2 = banner_arr[(i + 1) % banner_length]
        banner2 += banner_arr[i % banner_length]

        val = ""
        for i in range(25):
            val += "\n"
        for i in range(50):
            val += " "
        if p1_score >= win_score:
            val += banner1 + "| Player 1 Wins! |" + banner2
        else:
            if is_cpu:
                val += banner1 + "| CPU Wins! |" + banner2
            else:
                val += banner1 + "| Player 2 Wins! |" + banner2

        for i in range(25):
            val += "\n"
        print(val)
        sleep(1)
    system('clear')
    LOG_FILE.close()
    exit(0)
except KeyboardInterrupt:
    system('clear')
    LOG_FILE.close()
    exit(0)
