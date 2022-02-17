from time import sleep
from math import floor, sin, cos, radians, ceil
from sys import exit
from os import system
from pynput import keyboard

from gameEngine.classes import *
from gameEngine.utils import Logger

LOG_FILE = open("pong.log", "w")
logger = Logger(LOG_FILE)

win_score = int(input("Points to win: "))
is_cpu = not bool(int(input("How many players? | 1 or 2 | : ")) - 1)

p1_dir = Vector2(0, 0)
p2_dir = Vector2(0, 0)
display = Display(100, 50)
p1 = Line(10, Vector2.down(), Vector2(0,1), display)
p2 = Line(10, Vector2.down(), Vector2(99,1), display)

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
    global p2_dir
    global is_exit
    if key == keyboard.Key.esc:
        logger.log("bye")
        is_exit = True
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if not is_cpu:
        if k in [ 'up', 'down','w', 's']:
            if k == 'w':
                p1_dir = Vector2.up()
            if k == 'up':
                p2_dir = Vector2.up()
            if k == 'down':
                p2_dir = Vector2.down()
            if k == 's':
                p1_dir = Vector2.down()


    else:
        if k in [ 'w', 's']:
            if k == 'w':
                p1_dir = Vector2.up()
            if k == 's':
                p1_dir = Vector2.down()
        # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        #
def on_release(key):
        global p1_dir
        global p2_dir# stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if k in [ 'up', 'down','w','s']:
            if k == 'w':
                p1_dir = Vector2(0,0)
            if k == 'up':
                p2_dir = Vector2(0,0)
            if k == 'down':
                p2_dir = Vector2(0,0)
            if k == 's':
                p1_dir = Vector2(0,0)


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # start to listen on a separate thread

p1_score = 0
p2_score = 0

score = Text("0 - 0", Vector2.left(), Vector2(50,0), display)
ball = Ball(Vector2(50,25), Vector2(-1,0), display)
display.add_obj(p1_player.obj)
display.add_obj(ball)
display.add_obj(p2)
display.add_obj(score)
ball_dir = Vector2.left()
screen_bounds = Vector2(1,40)
try:
    while True:
        if is_exit:
            system('clear')
            LOG_FILE.close()
            exit(0)
        if is_cpu:
            if p1.pos.y <= screen_bounds.x and p1_dir.equals(Vector2.down()):
                p1_player.set_direction(p1_dir)
            elif p1.pos.y >= screen_bounds.y and p1_dir.equals(Vector2.up()):
                p1_player.set_direction(p1_dir)
            elif screen_bounds.x <= p1.pos.y <= screen_bounds.y:
                p1_player.set_direction(p1_dir)

        else:
            if p1.pos.y >= screen_bounds.y and p1_dir.equals(Vector2.up()):
                #p1.move(p1_dir)
                p1_player.set_direction(p1_dir)

            elif p1.pos.y <= screen_bounds.x and p1_dir.equals(Vector2.down()):
                #p1.move(p1_dir)
                p1_player.set_direction(p1_dir)
            elif screen_bounds.x <= p1.pos.y <= screen_bounds.y:
                #p1.move(p1_dir)
                p1_player.set_direction(p1_dir)
            if p2.pos.y >= screen_bounds.y and p2_dir.equals(Vector2.up()):
                #p2.move(p2_dir)
                p2_player.set_direction(p2_dir)

            elif p2.pos.y <= screen_bounds.x and p2_dir.equals(Vector2.down()):
                #p2.move(p2_dir)
                p2_player.set_direction(p2_dir)
            elif screen_bounds.x <= p2.pos.y <= screen_bounds.y:
                #p2.move(p2_dir)
                p2_player.set_direction(p2_dir)

        if ball.pos.x <= 1:
            if ball.pos.y >= p1.pos.y and ball.pos.y < p1.pos.y + p1.length:
                center = p1.pos.y + ceil(p1.length / 2)
                rot = ball.pos.y - center
                rot /= (p1.length / 2)
                rot *= 60
                x = cos(radians(rot))
                y = sin(radians(rot))
                #1,0
                ball.set_dir(Vector2(x, y))
            else:
                p2_score += 1
                score.set_value(f"{p1_score} - {p2_score}")
                ball.set_pos(Vector2(50,25))
                ball.set_dir(Vector2(1, 0))
        if ball.pos.x >= 99:
            if ball.pos.y >= p2.pos.y and ball.pos.y <= p2.pos.y + p2.length:
                center = p2.pos.y + ceil(p2.length / 2)
                rot = ball.pos.y - center
                rot /= (p2.length / 2)
                rot *= 60
                x = -1 * cos(radians(rot))
                y = sin(radians(rot))
                #-1,0
                ball.set_dir(Vector2(x, y))
            else:
                p1_score += 1
                score.set_value(f"{p1_score} - {p2_score}")
                ball.set_pos(Vector2(50,25))
                ball.set_dir(Vector2(1, 0))
        if ball.pos.y >= 50:
            x = ball.direction.x
            y = ball.direction.y
            ball.set_dir(Vector2(x, -1 * y))
        if ball.pos.y <= 0:
            x = ball.direction.x
            y = ball.direction.y
            ball.set_dir(Vector2(x, -1 * y))
        ball.move()
        if p1_score >= win_score or p2_score >= win_score:
            break
        #p1_player.update()
        display.update()
        p1_player.update()
        p2_player.update()

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
