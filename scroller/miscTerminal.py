import numpy as np
import random
from os import system
def make_gameboard():
    gameboard = [[]]
    for i in range(11):
        gameboard.append([])
        for j in range(11):
            tile_type = random.randint(0,100)
            if 0 <= tile_type < 60: 
                gameboard[i].append("|_|")
            elif 60 <= tile_type <= 80:
                gameboard[i].append("|&|")
            else:
                gameboard[i].append("|A|")
    under = gameboard[5][5]
    gameboard[5][5] = " O "
    return under, gameboard, (0, 0)

def print_gameboard(gameboard):
    system('clear')
    for i in range(len(gameboard)):
        print(gameboard[i])

def move(under, gameboard, coords, dir_x, dir_y):
    gameboard[5][5] = under
    _, new_gameboard, _ = make_gameboard()
    for i in range(11):
        for j in range(11):
            new_gameboard[i][j] = gameboard[((i + dir_y)%11)][((j + dir_x) %11)]
    under = new_gameboard[5][5]
    new_gameboard[5][5] = " O "
    a, b = coords
    adj_a = a + dir_x
    adj_b = b - dir_y
    def loop_val(val):
        if val == -6:
            val = 5
        elif val == 6:
            val = -5
        return val
    adj_a = loop_val(adj_a)
    adj_b = loop_val(adj_b)
    return under, new_gameboard, (adj_a, adj_b)

under, gameboard, coords = make_gameboard()

while(True):
    dir = input()
    val = []
    for i in dir:
        val.append(ord(i))
    if val == [27, 91, 65]:
        under, gameboard, coords = move(under, gameboard, coords, 0, -1)
    if val == [27, 91, 66]:
        under, gameboard, coords = move(under, gameboard, coords, 0, 1)
    if val == [27, 91, 68]:
        under, gameboard, coords = move(under, gameboard, coords, -1, 0)
    if val == [27, 91, 67]:
        under, gameboard, coords = move(under, gameboard, coords, 1, 0)
    print_gameboard(gameboard)
    print(coords)
