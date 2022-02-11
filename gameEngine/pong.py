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

win_score = int(input("Points to win: "))
is_cpu = not bool(int(input("How many players? | 1 or 2 | : ")) - 1)

p1_dir = Vector2(0, 0)
p2_dir = Vector2(0, 0)
is_exit = False
    

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
        if k in [ 'up', 'down']:
            if k == 'up':
                p1 = Vector2.up()
            if k == 'down':
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

display = Display(100, 50)
p1_score = 0
p2_score = 0
p1 = Line(10, Vector2.down(), Vector2(0,0), display)
p2 = Line(10, Vector2.down(), Vector2(99,0), display)
score = Text("0 - 0", Vector2.left(), Vector2(50,0), display)
ball = Ball(Vector2(50,25), Vector2(-1,0), display)
display.add_obj(p1)
display.add_obj(ball)
display.add_obj(p2)
display.add_obj(score)
ball_dir = Vector2.left()
try:
    while True:
        if is_exit:
            system('clear')
            LOG_FILE.close()
            exit(0)
        if is_cpu:
            p1.move(p1_dir)
        else:
            p1.move(p1_dir)
            p2.move(p2_dir)
        
        if ball.pos.x == 0:
            if ball.pos.y > p1.pos.y and ball.pos.y < p1.pos.y + p1.length:
                ball.set_dir(Vector2(1, 0))
            else:
                p2_score += 1
                score.set_value(f"{p1_score} - {p2_score}")
                ball.set_pos(Vector2(50,25))
        if ball.pos.x == 99:
            if ball.pos.y > p2.pos.y and ball.pos.y < p2.pos.y + p2.length:
                ball.set_dir(Vector2(-1, 0))
            else:
                p1_score += 1
                score.set_value(f"{p1_score} - {p2_score}")
                ball.set_pos(Vector2(50,25))
        ball.move()
        if p1_score >= win_score or p2_score >= win_score:
            break
        display.update()
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
        if p1 >= win_score:
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
