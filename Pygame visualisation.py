import pygame
import Game_math_functions as gm
import keyboard

pygame.font.init()
# pygame settings
background_colour = (201, 194, 109)
screen = pygame.display.set_mode((gm.x * 110 + 200, gm.y * 110 - 10))
pygame.display.set_caption("2048 game with AI")
font = pygame.font.SysFont("arial", 36)
font_score = pygame.font.SysFont("arial", 25)
# Variables
mass = []
mass = gm.mass_fill(mass)
key_flagd = 0
key_flagu = 0
key_flagl = 0
key_flagr = 0
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
            render = font_score.render(f"Your score:{gm.score}", True, (0, 0, 0))
            screen.blit(render, (gm.x * 110 + 3, 20))

    pygame.display.update()
