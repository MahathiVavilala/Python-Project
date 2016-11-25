import pygame, sys
from pygame.locals import *
import random
import game
pygame.init()

tiles = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def randomtile(tiles):
    rows = []
    columns = []
    for i in range(4):
        for j in range(4):
            if tiles[i][j] == 0:
                rows.append(i)
                columns.append(j)
    if len(rows) > 1:
        index = len(rows) - 1
        pos = random.choice(range(index))
        row = rows[pos]
        col = columns[pos]
        tiles[row][col] = 2
    elif len(rows) == 1:
        row = rows[0]
        col = columns[0]
        tiles[row][col] = 2
    else :
        tiles = tiles
    return (tiles)       

def up_move(tiles):
    i = 0
    for j in range(4):
        if tiles[i][j] !=0 or tiles[i + 1][j] != 0 or tiles[i + 2][j] != 0 or tiles[i + 3][j] != 0:
            
            if tiles[i][j] == 0 :
                for k in range(0, 3):                   
                    tiles[i + k][j] = tiles[i + k + 1][j] 
                tiles[i + 3][j] = 0
            if tiles[i + 1][j] == 0:
                for k in range(1, 3):
                    tiles[i + k][j] = tiles[i + k + 1][j]
                tiles[i + 3][j] = 0
            if tiles[i + 2][j] == 0:
                tiles[i + 2][j] = tiles[i + 3][j]
                tiles[i + 3][j] = 0
    return(tiles)

def up_merge(tiles):
    for j in range(4):
        for k in range(3):
            if tiles[k][j] == tiles[k + 1][j]:
                tiles[k][j] = 2 * tiles[k][j]
                tiles[k + 1][j] = 0
    return(up_move(tiles))

def down_move(tiles):
    i = 3
    for j in range(4):
        if tiles[i][j] !=0 or tiles[i - 1][j] != 0 or tiles[i - 2][j] != 0 or tiles[i - 3][j] != 0:

            if tiles[i][j] == 0 :
                for k in range(0, 3):
                    tiles[i - k][j] = tiles[i - (k + 1)][j]
                tiles[i - 3][j] = 0
            if tiles[i - 1][j] == 0:
                for k in range(1, 3):
                    tiles[i - k][j] = tiles[i - (k + 1)][j]
                tiles[i - 3][j] = 0
            if tiles[i - 2][j] == 0:
                tiles[i - 2][j] = tiles[i - 3][j]
                tiles[i - 3][j] = 0
    return(tiles)

def down_merge(tiles):
    for j in range(4):
        for k in reversed(range(3)):
            if tiles[k][j] == tiles[k + 1][j]:
                tiles[k + 1][j] = 2 * tiles[k][j]
                tiles[k][j] = 0
    return(down_move(tiles))

def left_move(tiles):
    j = 0
    for i in range(4):
        if tiles[i][j] !=0 or tiles[i][j + 1] != 0 or tiles[i][j + 2] != 0 or tiles[i][j + 3] != 0:
            if tiles[i][j] == 0 :
                for k in range(0, 3):
                    tiles[i][j + k] = tiles[i][j + k + 1]
                tiles[i][j + 3] = 0
            if tiles[i][j + 1] == 0:
                for k in range(1, 3):
                    tiles[i][j + k] = tiles[i][j + k + 1]
                tiles[i][j + 3] = 0
            if tiles[i][j + 2] == 0:
                tiles[i][j + 2] = tiles[i][j + 3]
                tiles[i][j + 3] = 0
    return(tiles)

def left_merge(tiles):
    for k in range(4):
        for j in range(3):
            if tiles[k][j] == tiles[k][j + 1]:
                tiles[k][j] = 2 * tiles[k][j]
                tiles[k][j + 1] = 0
    return(left_move(tiles))

def right_move(tiles):
    j = 3
    for i in range(4):
        if tiles[i][j] !=0 or tiles[i][j - 1] != 0 or tiles[i][j - 2] != 0 or tiles[i][j - 3] != 0:
            if tiles[i][j] == 0 :
                for k in range(0, 3):
                    tiles[i][j - k] = tiles[i][j - (k + 1)]
                tiles[i][j - 3] = 0
            if tiles[i][j - 1] == 0:
                for k in range(1, 3):
                    tiles[i][j - k] = tiles[i][j - (k + 1)]
                tiles[i][j - 3] = 0
            if tiles[i][j - 2] == 0:
                tiles[i][j - 2] = tiles[i][j - 3]
                tiles[i][j - 3] = 0
    return(tiles)

def right_merge(tiles):
    for k in range(4):
        for j in reversed(range(3)):
            if tiles[k][j] == tiles[k][j + 1]:
                tiles[k][j + 1] = 2 * tiles[k][j]
                tiles[k][j] = 0
    return(right_move(tiles))

 
game.printTiles(randomtile(tiles))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            game.printTiles(randomtile((up_merge(up_move(up_move(tiles))))))
        if keys[K_DOWN]:
            game.printTiles(randomtile(down_merge(down_move(down_move(tiles)))))
        if keys[K_LEFT]:
            game.printTiles(randomtile(left_merge(left_move(left_move(tiles)))))
        if keys[K_RIGHT]:
            game.printTiles(randomtile(right_merge(right_move(right_move(tiles)))))
        if any(tiles) == 2048:
            print("<<<<<<<<<< YOU WIN >>>>>>>>>>")
