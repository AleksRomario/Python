#!/usr/bin/env python3
print("--- Что такое Pygame. Каркас приложения, FPS")

import pygame
pygame.init()

WIDTH = 1100
HEIGHT = 700

pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
