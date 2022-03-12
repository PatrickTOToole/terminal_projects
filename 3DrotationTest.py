from time import sleep
from os import system
from gameEngine.classes import *
from gameEngine.utils import Logger

LOG_FILE = open("rotTest.log", "w")
logger = Logger(LOG_FILE)
display = Display(100, 50, 100)
line = Line3D(10, Vector3.down(), Vector3(10,10,0), display)
line2 = Line3D(10, Vector3.right(), Vector3(10,10,0), display)
display.add_obj(line)
display.add_obj(line2)
try:
    while True:
        display.update()
        line.set_direction((line.get_direction() + Vector3(1,0,0)).to_unit())
        line2.set_direction((line2.get_direction() + Vector3(1,0,0)).to_unit())

    system('clear')
    LOG_FILE.close()
    exit(0)
except KeyboardInterrupt:
    system('clear')
    LOG_FILE.close()
    exit(0)
