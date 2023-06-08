import pygame, random
from pygame.math import Vector2
from settings import *
#Creates class human
class Human(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Chooses a random location for the human
        self.x = random.randint(0, 14)
        self.y = random.randint(0, 14)
        self.location = pygame.math.Vector2(self.x, self.y)


        #Chooses a random number from 1 to 3 and sets the human's image based on this number
        number = random.randint(1, 3)
        if number == 1:
            self.image = pygame.image.load("hotlinebling1.png")
        if number == 2:
            self.image = pygame.image.load("hotlinebling2.png")
        if number == 3:
            self.image = pygame.image.load("hotlinebling3.png")

        pos = (self.x * tile_width, self.y * tile_height)
        self.rect = self.image.get_rect(topleft=pos)





