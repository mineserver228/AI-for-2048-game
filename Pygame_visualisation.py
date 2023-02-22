import random

import keyboard
import pygame

import Game_math_functions as gm

pygame.font.init()
# pygame settings
background_colour = (201, 194, 109)
screen = pygame.display.set_mode((gm.x * 110 + 300, gm.y * 110 - 10))
pygame.display.set_caption("2048 game with AI")
font = pygame.font.SysFont("arial", 36)
font_score = pygame.font.SysFont("arial", 25)
# Variables
mass = [[0] * gm.x for i in range(gm.y)]
mass = gm.add_blocks(mass)
max_score = 0
auto_click = False
keys = ["down", "up", "left", "right"]
actions = [gm.key_down, gm.key_up, gm.key_left, gm.key_right]
flags = [False, False, False, False]
# initialization of cell colors
gm.colours = gm.colours_init(gm.colours)
# loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_colour)

# keys
    for i, (key, action) in enumerate(zip(keys, actions)):
        if keyboard.is_pressed(key):
            if flags[i]:
                continue
            mass = action(mass)
            mass = gm.add_blocks(mass)
            flags[i] = True
        else:
            if flags[i]:
                flags[i] = False

    if auto_click:
        if not keyboard.is_pressed("space"):
            rand = random.randint(1, 4)
            if rand == 1:
                mass = gm.key_down(mass)
            if rand == 2:
                mass = gm.key_up(mass)
            if rand == 3:
                mass = gm.key_left(mass)
            if rand == 4:
                mass = gm.key_right(mass)
            mass = gm.add_blocks(mass)

    # Draw squares with numbers
    for i in range(gm.x):
        for g in range(gm.y):
            # colours not working
            colour = 0
            division = mass[g][i]
            while not division < 2:
                colour += 1
                division = division // 2
            pygame.draw.rect(screen,
                (gm.colours[colour * 3 + 1], gm.colours[colour * 3 + 2], gm.colours[colour * 3 + 3]),
                (110 * i, 110 * g, 100, 100))
            if not mass[g][i] == 0:
                render = font.render(f"{mass[g][i]}", True, (0, 0, 0))
                screen.blit(render, (110 * i + 30, 110 * g + 30))
            render = font_score.render(f"Score:{gm.score}", True, (0, 0, 0))
            screen.blit(render, (gm.x * 110 + 3, 5))
            if max_score < gm.score:
                max_score = gm.score
            render = font_score.render(f"Best score:{max_score}", True, (0, 0, 0))
            screen.blit(render, (gm.x * 110 + 3, 30))

    pygame.display.update()
