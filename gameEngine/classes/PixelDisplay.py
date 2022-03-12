from __future__ import print_function
from drawille import Canvas
from math import sin, radians
from os import system
from time import sleep

c = Canvas()

i = 0
class PixelDisplay:
    def __init__(self, refresh):
        self.refresh = refresh / 60

while True:
    i %= 10000
    for x in range(0, 1800, 10):
        x += i
        c.set(x / 10, 10 + sin(radians(x)) * 100)
        c.set(x / 10 + 1, 10 + sin(radians(x)) * 100)



    i += 10
    print(c.frame())
    c.clear()
    sleep(0.01)
    system('clear')
