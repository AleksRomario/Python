#!/usr/bin/env python3
"""
PYGAME SCELETON
"""

#IMPORTS
import pygame, sys, random

#COSTANTS
WIDTH, HEIGHT = 800, 600  
FPS = 30 
CAPTION = "Caption name"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#INITIALIZING 
pygame.init() # main init
pygame.mixer.init() # sound init
main_screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption(CAPTION)
FramePerSec = pygame.time.Clock() # track the speed


#GAME LOOP
running_game = True 
while running_game:
    # 0. Keep loo[p runnig at the right speed   
    FramePerSec.tick(FPS)

    # 1. Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False


    # 2. Update


    # 3. Draw/render
    main_screen.fill(BLACK)
    
    # make sure to do it last think after drapwing all. 
    pygame.display.flip()



pygame.quit()



"""
if __name__ == "__main__":
    print("started as main file")
"""
