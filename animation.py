from math import floor, sin, cos, radians, ceil
from sys import exit
from os import system
from pynput import keyboard

from gameEngine.classes import *

display = Display(100, 50, 100)
box = Box(5,5,10,10,display)
display.add_obj(box)
while True:
    display.update()
