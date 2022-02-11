from time import sleep
from math import floor
from sys import exit
from os import system
from pynput import keyboard
from classes.Vector2 import Vector2
from classes.Line import Line
from classes.Display import Display
from classes.Box import Box
from classes.Dot import Dot
from classes.Ball import Ball
from classes.Text import Text
from utils.Logger import Logger

LOG_FILE = open("log", "w")
logger = Logger(LOG_FILE)


var_dir = Vector2(0, 0)
is_exit = False
    

def on_press(key):
    global var_dir
    global is_exit
    if key == keyboard.Key.esc:
        logger.log("bye")
        is_exit = True
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in [ 'up', 'down']:
        if k == 'up':
            var_dir = Vector2.up()
        if k == 'down':
            var_dir = Vector2.down()
        # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        #
def on_release(key):
        global var_dir  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if k in [ 'up', 'down']:
            if k == 'up':
                var_dir = Vector2(0,0)
            if k == 'down':
                var_dir = Vector2(0,0)
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # start to listen on a separate thread

display = Display(100, 50)
player_score = 0
cpu_score = 0
ponger = Line(10, Vector2.down(), Vector2(0,0), display)
cpu = Line(10, Vector2.down(), Vector2(99,0), display)
score = Text("0 - 0", Vector2.left(), Vector2(50,0), display)
ball = Ball(Vector2(50,25), Vector2(-1,0), display)
display.add_obj(ponger)
display.add_obj(ball)
display.add_obj(cpu)
display.add_obj(score)
ball_dir = Vector2.left()
try:
    while True:
        if is_exit:
            system('clear')
            LOG_FILE.close()
            exit(0)
        ponger.move(var_dir)
        if ball.pos.x == 0:
            if ball.pos.y > ponger.pos.y and ball.pos.y < ponger.pos.y + ponger.length:
                ball.set_dir(Vector2(1, 0))
            else:
                cpu_score += 1
                score.set_value(f"{player_score} - {cpu_score}")
                ball.set_pos(Vector2(50,25))
        if ball.pos.x == 99:
            if ball.pos.y > cpu.pos.y and ball.pos.y < cpu.pos.y + cpu.length:
                ball.set_dir(Vector2(-1, 0))
            else:
                player_score += 1
                score.set_value(f"{player_score} - {cpu_score}")
                ball.set_pos(Vector2(50,25))
        ball.move()
        if player_score >= 10 or cpu_score >= 10:
            break
        display.update()
        sleep(0.01)
    system('clear')
    banner_arr = ["_","-","‾","-"]
    banner_length = len(banner_arr)
    for i in range(10):
        banner = banner_arr[i % banner_length]
        banner += banner_arr[(i + 1) % banner_length]

        val = ""
        for i in range(25):
            val += "\n"
        for i in range(50):
            val += " "
        if player_score >= 10:
            val + banner + "Player Wins!" + banner
        else:
            val + banner + "Player Wins!" + banner
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
