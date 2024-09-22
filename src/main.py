import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pygame
from pytmx import util_pygame

background_colour = ((134, 102, 217, 1))

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("PyGame RPGs")

screen.fill(background_colour)

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False