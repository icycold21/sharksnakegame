import pygame, random
from pygame.math import Vector2
from settings import *

#Creates class Shark
class Shark(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10), Vector2(8,10), Vector2(9,10)]
        self.screen = screen
        self.direction = Vector2(-1,0)
#Draws shark on screen, block by block, and changes its graphic depending on its direction/relationship to other blocks
    def draw_shark(self, screen):
        for block in self.body:
            block_sprite = pygame.Rect(block.x * tile_width, block.y * tile_height, tile_width, tile_height)
            if block == self.body[0]:
                if self.direction == [1, 0]:
                    screen.blit(pygame.image.load("graphics/righthead.png"), block_sprite)
                elif self.direction == [-1, 0]:
                    screen.blit(pygame.image.load("graphics/lefthead.png"), block_sprite)
                elif self.direction == [0, 1]:
                    screen.blit(pygame.image.load("graphics/downhead.png"), block_sprite)
                elif self.direction == [0, -1]:
                    screen.blit(pygame.image.load("graphics/uphead.png"), block_sprite)

            else:
                index_value = self.body.index(block) - 1
                block_direction = block - self.body[index_value]

                if block != self.body[-1]:
                    if block_direction == [1, 0]:
                        screen.blit(pygame.image.load("graphics/middlemiddle.png"), block_sprite)
                    elif block_direction == [-1, 0]:
                        screen.blit(pygame.image.load("graphics/middlemiddle.png"), block_sprite)
                    elif block_direction == [0, 1]:
                        screen.blit(pygame.image.load("graphics/middlemiddle.png"), block_sprite)
                    elif block_direction == [0, -1]:
                        screen.blit(pygame.image.load("graphics/middlemiddle.png"), block_sprite)

                else:
                    if block_direction == [1, 0]:
                        screen.blit(pygame.image.load("graphics/righttail.png"), block_sprite)
                    elif block_direction == [-1, 0]:
                        screen.blit(pygame.image.load("graphics/lefttail.png"), block_sprite)
                    elif block_direction == [0, 1]:
                        screen.blit(pygame.image.load("graphics/downtail.png"), block_sprite)
                    elif block_direction == [0, -1]:
                        screen.blit(pygame.image.load("graphics/uptail.png"), block_sprite)



    #Function code taken from YouTube video (Clear Code)
    # - moves the shark by creating a new body moved in the relevant direction
    def move_shark(self):
        #creating new body list
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        print(self.body)

    #Gets input from the user about which keys they press
    #(arrow keys) in order to move the shark in the right direction
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.direction = Vector2(0, 1)
        if keys[pygame.K_UP]:
            self.direction = Vector2(0, -1)
        if keys[pygame.K_LEFT]:
            self.direction = Vector2(-1, 0)
        if keys[pygame.K_RIGHT]:
            self.direction = Vector2(1, 0)


