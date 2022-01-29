#imports!
from re import TEMPLATE
from tkinter import N
from pygame.constants import K_KP_ENTER, K_RETURN, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, TIMER_RESOLUTION, K_a, K_c, K_d, K_s, K_w, K_l, K_p
from pickle import FALSE
import numpy as np
from numpy.random.mtrand import rand
import pygame

pygame.init()

#variables!
height = 800
width = 1000

#colors!
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (154,205,50)
white = (255,255,255)

#canvas!
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("BounceGame!")

#dotsSpreadWave!
def dotsSpread(numDots, vecX, vecY):
    i = 0
    while i < numDots:
        pygame.draw.rect(dis, white, [vecX, vecY, 2, 2])
        i = i + 1

def gameLoop():
    vecX = []
    vecY = []

    mousePosX = 0
    mousePosY = 0
    numberOfElem = 0
    i = 0

    gameOver = False

    while not gameOver:
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                gameOver = True

            #drawing!
            if event.type==pygame.KEYDOWN:
                if event.key== K_l and numberOfElem%2 == 0 and i < len(vecX) :
                    pygame.draw.aaline(dis, white, [vecX[0+i], vecY[0+i]], [vecX[i+1], vecY[i+1]], True)
                    i = i + 2
                if event.key== K_c and numberOfElem%2 == 0 and i < len(vecX) :
                    pygame.draw.circle(dis, white, [vecX[0+i], vecY[0+i]], np.sqrt(np.abs(vecX[0+i]-vecX[i+1]) * np.abs(vecX[0+i]-vecX[i+1]) 
                    + np.abs(vecY[0+i]-vecY[i+1]) * np.abs(vecY[0+i]-vecY[i+1])), 1)
                    i = i + 2
                if event.key== K_p and numberOfElem%2 == 0 and i < len(vecX):
                    dotsSpread(25, vecX[0+i], vecY[0+i])
                    i = i + 2

            #localisation!
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePosX = pygame.mouse.get_pos()[0]
                mousePosY = pygame.mouse.get_pos()[1]

                vecX.append(mousePosX)
                vecY.append(mousePosY)

                print(vecX[numberOfElem], vecY[numberOfElem])
                numberOfElem = numberOfElem + 1
            
        pygame.display.update()

gameLoop()
pygame.quit()
quit()

