import numpy
import pygame
import time
import random

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, K_a, K_d, K_s, K_w

pygame.init();

#variables!--------
height = 800
width = 1000

gamespeed = 15

#colors!
red = (255, 0, 0)
black = (0, 0, 0)

#canvas!
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodge the walls!")

#wall generation!
def wall (WallArray, SpawnDisty1):
    i = 0
    while i < len(WallArray):
        pygame.draw.rect(dis, red, [WallArray[i], SpawnDisty1, 10, 10])
        i += 1

def wallSpawn(WallArray, SpawnDisty1):
    gaps = round(random.randrange(0, 300))
    x = 0
    randvaluey = round(random.randrange(gaps, width) / 10) * 10
    while x < ((width/10) - gaps):
        randvaluey = round(random.randrange(gaps, width) / 10) * 10
        x += 1

    WallArray.append(randvaluey)
    wall(WallArray, SpawnDisty1)

#player!
def player(x1p, y1p):
    pygame.draw.rect(dis, red, [x1p, y1p, 10, 10])

#gameloop!
def gameloop():

    x1 = width/2
    y1 = height/2

    x1_change = 0
    y1_change = 0
    SpawnDisty1 = -50
    WallArray = []

    gameOver = False
    
    while not gameOver:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver = True

            if event.type==pygame.KEYDOWN:
                if event.key == K_w:
                    y1_change = -10;
                    x1_change = 0;
                elif event.key == K_s:
                    y1_change = 10;
                    x1_change = 0;
                elif event.key == K_a:
                    y1_change = 0;
                    x1_change = -10;
                elif event.key == K_d:
                    y1_change = 0;
                    x1_change = 10;

                if event.key == K_UP:
                    y1_change = -20;
                    x1_change = 0;
                elif event.key == K_DOWN:
                    y1_change = 20;
                    x1_change = 0;
                elif event.key == K_LEFT:
                    y1_change = 0;
                    x1_change = -20;
                elif event.key == K_RIGHT:
                    y1_change = 0;
                    x1_change = 20;

        x1 += x1_change
        y1 += y1_change

        #clock!
        clock = pygame.time.Clock() 
        clock.tick(gamespeed)
        SpawnDisty1 += 10

        #drawing!
        dis.fill(black)
        player(x1, y1)
        wallSpawn(WallArray, SpawnDisty1)

        #walls!

        pygame.display.update()

    #termination
    pygame.quit()
    quit()

gameloop()





