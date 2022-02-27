import pygame
import numpy as py
import math
import random
import time

pygame.init()

#variables!
Side = 350
Degree = 8
width = 2*Side
heigth = 2*Side
cX = width/2
cY = heigth/2
white = (255,255,255)
blue = (0,0,255)
#display!
dis = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Recursive!')

#methods!
def systemPause():

    gameOver = False
    while not gameOver:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()


def recursiveSquareDimensions(Degree, sideLength, cX, cY):

    if Degree <= 1:
        #pygame.time.wait(5)
        pygame.draw.rect(dis, white, [cX - sideLength/2, cY - sideLength/2, sideLength, sideLength])
        pygame.display.update()
        return
    
    Degree = Degree - 1
    recursiveSquareDimensions(Degree, sideLength/2, cX - sideLength/2, cY - sideLength/2)
    recursiveSquareDimensions(Degree, sideLength/2, cX - sideLength/2 + sideLength, cY - sideLength/2)
    recursiveSquareDimensions(Degree, sideLength/2, cX - sideLength/2, cY - sideLength/2 + sideLength)
    recursiveSquareDimensions(Degree, sideLength/2, cX - sideLength/2 + sideLength, cY - sideLength/2 +sideLength)

    #pygame.time.wait(10)
    pygame.draw.rect(dis, white, [cX - sideLength/2, cY - sideLength/2, sideLength, sideLength])
    pygame.draw.rect(dis, blue, [cX - sideLength/2, cY - sideLength/2, sideLength, sideLength], 1)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
          
recursiveSquareDimensions(Degree, Side, cX, cY)
systemPause()
pygame.display.update()
pygame.quit()
quit()
