import pygame
from pygame.transform import scale, rotate


class Spaceship(pygame.sprite.Sprite):

    def __init__(self, sprite, position):
        super().__init__()
        self.axes_x = float(position[0])
        self.axes_y = float(position[1])

        self.sprite = pygame.image.load(sprite).convert_alpha()

    def translate(self, keys):
        if keys[pygame.K_w]:
            self.axes_y -= 1 / 6
            print("Move W")
    
        if keys[pygame.K_s]:
            self.axes_y += 1 / 6
            print("Move S")

        if keys[pygame.K_a]:
            self.sprite = rotate(self.sprite, 90)
            print("Rotate A")

        if keys[pygame.K_d]:
            self.sprite = rotate(self.sprite, 90)
            print("Rotate D")

        if keys[pygame.K_SPACE]:
            pass





