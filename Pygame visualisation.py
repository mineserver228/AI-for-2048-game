import pygame
import Game_math_functions as gm
import keyboard

# pygame settings
background_colour = (201, 194, 109)
screen = pygame.display.set_mode((gm.x * 110 + 10, gm.y * 110 + 10))
pygame.display.set_caption("2048 game with AI")
# Variables
mass = []
mass = gm.mass_fill(mass)
key_flagd = 0
key_flagu = 0
key_flagl = 0
key_flagr = 0

# loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_colour)
    # keys
    # key DOWN
    if keyboard.is_pressed("down"):
        if key_flagd != 1:
            key_flagd = 1
            mass = gm.key_down(mass)
            mass = gm.add_blocks(mass)
    if not keyboard.is_pressed("down"):
        if key_flagd == 1:
            key_flagd = 0
    # key UP
    if keyboard.is_pressed("up"):
        if key_flagu != 1:
            key_flagu = 1
            mass = gm.key_up(mass)
            mass = gm.add_blocks(mass)
    if not keyboard.is_pressed("up"):
        if key_flagu == 1:
            key_flagu = 0
    # key LEFT
    if keyboard.is_pressed("left"):
        if key_flagl != 1:
            key_flagl = 1
            mass = gm.key_left(mass)
            mass = gm.add_blocks(mass)
    if not keyboard.is_pressed("left"):
        if key_flagl == 1:
            key_flagl = 0
    # key RIGHT
    if keyboard.is_pressed("right"):
        if key_flagr != 1:
            key_flagr = 1
            mass = gm.key_right(mass)
            mass = gm.add_blocks(mass)
    if not keyboard.is_pressed("right"):
        if key_flagr == 1:
            key_flagr = 0

    # Draw sqares with numbers
    for i in range(gm.x):
        for g in range(gm.y):
            # colours not working
            pygame.draw.rect(screen,
                        (255, 255 - mass[g][i] * 3, 255 - mass[g][i] * 3),
                        (110 * i, 110 * g, 100, 100))
    pygame.display.update()
