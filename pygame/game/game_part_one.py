#!/usr/bin/env python3
"""
https://www.youtube.com/watch?v=jO6qQDNa2UY&t=481s

"""

# Imports
import pygame
import os
from settings import *

pygame.init()

ISAAC_IMAGE = pygame.image.load(os.path.join('img', 'isaac.png'))
ISAAC = pygame.transform.scale(ISAAC_IMAGE, (ISAAC_WIDTH, ISAAC_HEIGHT))
FPS_FONT = pygame.font.Font(os.path.join('font', 'upheaval', 'upheavtt.ttf'), 36)

# Creating window to work on
main_window = pygame.display.set_mode((WIDTH, HEIGHT))
# We can give Caption to our window and so on...
pygame.display.set_caption(WINDOW_TITLE)


# Separate section that gonna be just drawing.
def draw_window(isaac, fps="0"):
    # fill window with colour
    main_window.fill(WHITE)

    # draw the character
    main_window.blit(ISAAC, (isaac.x, isaac.y))

    # draw FPS counter
    fps_box = FPS_FONT.render(f'{fps:2.2f}', False, (0, 0, 0))
    main_window.blit(fps_box, (535, 10))

    # update screen         
    pygame.display.update()


def handle_isaac_movement(keys_pressed, isaac):
    if keys_pressed[pygame.K_a]:  # left key pressed
        isaac.x -= ISAAC_SPEED
    if keys_pressed[pygame.K_w]:  # up key pressed
        isaac.y -= ISAAC_SPEED
    if keys_pressed[pygame.K_d]:  # right key pressed
        isaac.x += ISAAC_SPEED
    if keys_pressed[pygame.K_s]:  # down key pressed
        isaac.y += ISAAC_SPEED


# Main program loop


def main():
    # rectangle representing Issac 
    isaac = pygame.Rect(WIDTH / 2 - ISAAC_WIDTH / 2, HEIGHT / 2 - ISAAC_HEIGHT / 2, ISAAC_WIDTH, ISAAC_HEIGHT)

    # defying clock object to control FPS
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit button has been pressed!")
                run = False
        keys_pressed = pygame.key.get_pressed()
        handle_isaac_movement(keys_pressed, isaac)

        # game.time.Clock.get_fps()  -> float Compute your game's framerate (in frames per second). It is computed by
        # averaging the last ten calls to Clock.tick().
        current_fps = clock.get_fps()

        draw_window(isaac, fps=current_fps)

    # do smt ou of a main loop
    pygame.quit()


if __name__ == "__main__":
    main()
