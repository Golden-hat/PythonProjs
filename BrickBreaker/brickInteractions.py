import numpy as np
import pygame
import math
import time

pygame.init()

#variables!
heigth = 800
width = 1000
squareHeight = 20
squareWidth = 40

GroupBlock = []

#colors!
black = (0, 0, 0)
white = (255, 255, 255)
red = (100, 0, 0)

#display!
dis = pygame.display.set_mode((width,heigth))
pygame.display.set_caption('BrickBreaker!')

#functions!
def blockRow(timesX, timesY):
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

class block:
    def __init__(self, posX, posY, stats):
        self.positionX = posX
        self.positionY = posY
        self.status = stats

    def set_status(self, x):
        self.status = x
        
def game():

    gameover = False
    vecX = 0
    vecY = 0
    numberOfElem = 0

    j = 0
    displacementX = 0
    displacementY = 0

    Ysquares = 17
    Xsquares = 25

    while j < Ysquares:
        i = 0
        displacementX = 0
        while i < Xsquares:
            GroupBlock.append(block(displacementX, displacementY, True))
            displacementX = displacementX +squareWidth
            i = i + 1
        displacementY = displacementY + squareHeight
        j = j + 1

    while not gameover:
        dis.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True

            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePosX = pygame.mouse.get_pos()[0]
                mousePosY = pygame.mouse.get_pos()[1]

                vecX = mousePosX
                vecY = mousePosY

                print(vecX, vecY)
                numberOfElem = numberOfElem + 1

        blockRow(Xsquares, Ysquares)

        #logic!
        j = 0
        while j < len(GroupBlock):
            if (vecX > GroupBlock[j].positionX 
            and vecX <= GroupBlock[j].positionX + squareWidth 
            and vecY > GroupBlock[j].positionY 
            and vecY <= GroupBlock[j].positionY + squareHeight 
            and GroupBlock[j].status is True):
                GroupBlock[j].set_status(False)
            j = j + 1

        i = 0
        while i < len(GroupBlock):
            if (GroupBlock[i].status is False):
                pygame.draw.rect(dis, black, [GroupBlock[i].positionX, GroupBlock[i].positionY, squareWidth, squareHeight], 1)
            i = i + 1
        
        pygame.display.update()

game()
pygame.quit()
quit()