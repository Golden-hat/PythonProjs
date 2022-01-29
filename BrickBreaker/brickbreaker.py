from asyncio.windows_events import NULL
import numpy as np
import pygame
import math
import time
from pygame.constants import K_r

pygame.init()

#variables!
height = 800
width = 1000

squareHeight = 20
squareWidth = 40

cubeArray = []
colArray = []

speed = 60

#colors!
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (154, 205, 50)
white = (255, 255, 255)

#display!
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("brickBreaker")

#blocks!
def blockRow(timesX, timesY, localized):
    k = 0
    j = 0
    displacementX = 0
    displacementY = 0

    while j < timesY:
        i = 0
        displacementX = 0
        while i < timesX:
            pygame.draw.rect(dis, white, [0+displacementX, 0+displacementY, squareWidth, squareHeight], 1)
            displacementX = displacementX +squareWidth
            i = i + 1
            k = k + 1
        displacementY = displacementY + squareHeight
        j = j + 1
        
#gameloop!
def gameLoop():
    
    gameOver = False
    iniPosXBall = 500
    iniPosYBall = 500
    dispXBall = 0
    dispYBall = 0
    j = 0

    while not gameOver:
        
        dis.fill(black)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver = True

        #Ball!
        colRect = pygame.Rect(iniPosXBall, iniPosYBall+j, 1, 1)
        j = j - 3

        #collision!
        localized = 0
        while localized < len(cubeArray):
            if pygame.Rect.colliderect(cubeArray[localized], colRect) == True:
                cubeArray.pop(localized)
            localized = localized + 1

        blockRow(25, 12, localized)
        pygame.draw.rect(dis, white, [iniPosXBall, iniPosYBall+j, 1, 1])
        pygame.display.update()

        clock = pygame.time.Clock() 
        clock.tick(speed)

gameLoop()
pygame.quit()
quit()