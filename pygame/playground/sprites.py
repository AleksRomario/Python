#!/usr/bin/env python3
"""
PYGAME BASE https://www.youtube.com/watch?v=fcryHcZE_sM

SPRITE size in Isaac  is 32 x 32


DUNGEON --> 15 (480px) x 9 (288px) tiles
W - walls
D - doors
G - game field

W W W W W W W D W W W W W W W
W G G G G G G G G G G G G G W
W G G G G G G G G G G G G G W
W G G G G G G G G G G G G G W
D G G G G G G G G G G G G G D
W G G G G G G G G G G G G G W
W G G G G G G G G G G G G G W
W G G G G G G G G G G G G G W
W W W W W W W D W W W W W W W



"""

# IMPORTS

import pygame
import os
from pygame.locals import *

# CONSTANTS
WIDTH, HEIGHT = 800, 600
FPS = 30
CAPTION = "Caption name"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets (sounds and images)
# default game folder
game_folder = os.path.dirname(__file__)
# define game folder, create image folder for our assets
img_folder = os.path.join(game_folder, "img")


# ASSETS SETUP
# Isaac (Sprite) class should be(typeof=pygame.sprite.Sprite)
class Isaac(pygame.sprite.Sprite):
    # sprite for the player

    def __init__(self):
        # required line of code to have our sprite:
        pygame.sprite.Sprite.__init__(self)
        # required properties:
        # loaded image returning (self.image) typeof==pygame.Surface
        self.image = pygame.image.load(os.path.join(img_folder, 'isaac-binding-resource-pack.png')).convert_alpha()

        # cropped = pygame.Surface((80, 80))
        # self.image = cropped.blit(self.image, (0, 0), (30, 30, 80, 80))

        # eliminate transparent background (color to eliminate). Or use convert_alpha() after loading the object
        # #print("self.image.get_colorkey() = ", self.image.get_colorkey())
        # self.image.set_colorkey(BLACK)
        # print("self.image.get_colorkey() = ", self.image.get_colorkey())
        self.rect = self.image.get_rect()
        # print("self.rect = ", self.rect)
        # self.rect =  <rect(0, 0, 1484, 808)>
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        # try to see object attributes
        # print(dir(self.rect))
        # print(dir(self.image))
        # print(Isaac.__dict__)

    def update(self):
        self.rect.x += 1
        if self.rect.left > WIDTH:
            self.rect.right = 0


# INITIALIZING
pygame.init()  # main init
pygame.mixer.init()  # sound init
main_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
FramePerSec = pygame.time.Clock()  # track the speed

# Before all starts, making group of sprites (blank at the moment)
all_sprites = pygame.sprite.Group()
isaac = Isaac()
all_sprites.add(isaac)

# GAME LOOP
running_game = True
while running_game:
    # 0. Keep loop run at the right speed
    FramePerSec.tick(FPS)

    # 1. Process input (events)
    for event in pygame.event.get():
        if event.type == QUIT:
            running_game = False

    # 2. Update
    all_sprites.update()

    # 3. Draw/render
    # fill background color
    main_screen.fill(WHITE)
    all_sprites.draw(main_screen)

    # make sure to do it last think after drawing all.
    pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    print("started as main file")
