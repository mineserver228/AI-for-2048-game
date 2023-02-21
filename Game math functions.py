import random
import keyboard
import pygame

x = 5
y = 5
mass = []


# filling game desk at the start
def mass_fill(array):
    m = []
    for i in range(x):
        m.append(0)
    for i in range(y):
        array.append(m.copy())
    if random.randint(0, 1) == 0:
        array[random.randint(0, x - 1)][random.randint(0, y - 1)] = 4
    elif random.randint(0, 1) == 0:
        array[random.randint(0, x - 1)][random.randint(0, y - 1)] = 2
    else:
        array[random.randint(0, x - 1)][random.randint(0, y - 1)] = 2
        array[random.randint(0, x - 1)][random.randint(0, y - 1)] = 2
    return array


# colculating, when you click key "right"
def key_right(array):
    for i in range(x - 1):
        for g in range(y):
            if array[g][i + 1] == 0:
                array[g][i + 1] = array[g][i]
                array[g][i] = 0
            elif array[g][i + 1] == array[g][i]:
                array[g][i + 1] *= 2
                array[g][i] = 0
    return array


# colculating, when you click key "left"
def key_left(array):
    for i in range(x - 1):
        for g in range(y):
            if array[g][x - 2 - i] == 0:
                array[g][x - 2 - i] = array[g][x - 1 - i]
                array[g][x - 1 - i] = 0
            elif array[g][x - 2 - i] == array[g][x - 1 - i]:
                array[g][x - 2 - i] *= 2
                array[g][x - 1 - i] = 0
    return array


# colculating, when you click key "dawn"
def key_dawn(array):
    for i in range(y - 1):
        for g in range(x):
            if array[i + 1][g] == 0:
                array[i + 1][g] = array[i][g]
                array[i][g] = 0
            elif array[i + 1][g] == array[i][g]:
                array[i + 1][g] *= 2
                array[i][g] = 0
    return array


# colculating, when you click key "up"
def key_up(array):
    for i in range(y - 1):
        for g in range(x):
            if array[y - 2 - i][g] == 0:
                array[y - 2 - i][g] = array[y - 1 - i][g]
                array[y - 1 - i][g] = 0
            elif array[y - 2 - i][g] == array[y - 1 - i][g]:
                array[y - 2 - i][g] *= 2
                array[y - 1 - i][g] = 0
    return array


def add_blocks(array):
    for i in range(random.randint(1, 2)):
        randx = random.randint(0, x - 1)
        randy = random.randint(0, y - 1)
        while not array[randy][randx] == 0:
            randx = random.randint(0, x - 1)
            randy = random.randint(0, y - 1)
        if random.randint(0, 1) == 0:
            array[randy][randx] = 2
        else:
            array[randy][randx] = 4
    return array

