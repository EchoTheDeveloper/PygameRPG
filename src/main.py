import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# imports dependencies
import pygame
from pytmx import util_pygame

# Define the background colour
# using RGB color coding
background_colour = ((134, 102, 217, 1))

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((800, 600))

# Set the caption of the screen
pygame.display.set_caption("PyGame RPGs")

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False