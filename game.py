import pygame, sys
import random
from pygame.locals import *
pygame.init()

WIDTH = 420
HEIGHT = 420

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
SCREEN = pygame.display.get_surface()
pygame.display.set_caption('SUPER 2048')

def printTiles(tiles):
    cordinates = [0, 110, 220, 330]
    w = 100
    for i,r in enumerate(cordinates):
        for j,c in enumerate(cordinates):
            tile = pygame.draw.rect(SCREEN, (255, 250, 205), (r, c, w, w))
            if tiles[j][i] != 0:
                if tiles[j][i] in [2, 4, 8]:
                    label = font2.render(str(tiles[j][i]), 0, (0, 128, 128))
                elif tiles[j][i] in [16, 32, 64]:
                    label = font16.render(str(tiles[j][i]), 0, (199, 21, 147))
                elif tiles[j][i] in [128, 256, 512]:
                    label = font128.render(str(tiles[j][i]), 0, (138, 43, 226))
                elif tiles[j][i] == 1024:
                    label = font1024.render(str(tiles[j][i]), 0, (128, 0, 0))
                elif tiles[j][i] >= 2048 :
                    label = font2048.render(str(tiles[j][i]), 0, (0, 0, 139))
                else:
                    label = fontx.render('X', 0, (255, 0, 0))
                WINDOW.blit(label, tile)
    pygame.display.update()

tiles = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
font2 = pygame.font.SysFont("comicsansms", 110)
font16 = pygame.font.SysFont("comicsansms", 90)
font128 = pygame.font.SysFont("comicsansms", 70)
font1024 = pygame.font.SysFont("comicsansms", 50)
font2048 = pygame.font.SysFont("comicsansms", 45)
fontx = pygame.font.SysFont("comicsansms", 110)
