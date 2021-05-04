import pygame
from pygame.constants import K_ESCAPE
from starship import Spaceship
import os.path

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN])
window = 1200, 600
fps = 30

display = pygame.display.set_mode(window, pygame.DOUBLEBUF | pygame.HWSURFACE)

SPACESHIP = Spaceship(os.path.join("images", "spaceship.png"), (window[0] / 4, window[1] / 2))
BACKGROUND = pygame.image.load(os.path.join("images", "background.png")).convert()

while True:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in events:
        if event.type ==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit() 
    
    SPACESHIP.translate(keys)

    display.blit(BACKGROUND, (0,0))
    BACKGROUND.blit(SPACESHIP.sprite, (SPACESHIP.axes_x, SPACESHIP.axes_y))

    pygame.display.update()

d
