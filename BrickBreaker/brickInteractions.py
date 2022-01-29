from email.headerregistry import Group
import numpy as np
import pygame
import math
import time
import random

pygame.init()

#variables!
heigth = 800
width = 1000
squareHeight = 20
squareWidth = 40
speed = 300
font_style = pygame.font.SysFont(None, 20)
font_style2 = pygame.font.SysFont(None, 50)

#colors!
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#display!
dis = pygame.display.set_mode((width,heigth))
pygame.display.set_caption('BrickBreaker!')

#functions!
class block:
    def __init__(self, posX, posY, stats):
        self.positionX = posX
        self.positionY = posY
        self.status = stats

    def set_status(self, x):
        self.status = x

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [30, 750])

def message2(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [900, 750])

def message3(msg,color):
    mesg = font_style2.render(msg, True, color)
    dis.blit(mesg, [width/4+200, heigth/4+200])

def message4(msg,color):
    mesg = font_style2.render(msg, True, color)
    dis.blit(mesg, [width/4, heigth/4+300])

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
        
def game():

    gameover = False

    j = 0
    displacementX = 0
    displacementY = 0

    Ysquares = 20
    Xsquares = 25

    playerX = 400
    playerY = 650
    changeX = 0

    vecX = 500
    vecY = 500
    changeBx = 0
    changeBy = 1

    numBalls = 1

    score = -1

    GroupBlock = []
    
    while j < Ysquares:
        i = 0
        displacementX = 0
        while i < Xsquares:
            GroupBlock.append(block(displacementX, displacementY, True))
            displacementX = displacementX +squareWidth
            i = i + 1
        displacementY = displacementY + squareHeight
        j = j + 1

    #gameloop!
    while not gameover:
        dis.fill(black)

        #instructions!
        message("A/D keys to move LEFT or RIGHT, S key to STOP. Also works with <-, DOWN, -> .", white)

        #Score!
        if score != -1:
            message2("Score: " + str(score), white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changeX = -1.5
                elif event.key == pygame.K_RIGHT:
                    changeX = 1.5 
                if event.key == pygame.K_a:
                    changeX = -1.5
                elif event.key == pygame.K_d:
                    changeX = 1.5
                if event.key == pygame.K_s:
                    changeX = 0
                elif event.key == pygame.K_DOWN:
                    changeX = 0


        playerX = playerX + changeX

        blockRow(Xsquares, Ysquares)

        #logic!
        j = 0
        while j < len(GroupBlock):
            if (vecX >= GroupBlock[j].positionX 
            and vecX <= GroupBlock[j].positionX + squareWidth 
            and vecY >= GroupBlock[j].positionY 
            and vecY <= GroupBlock[j].positionY + squareHeight 
            and GroupBlock[j].status is True):
                GroupBlock[j].set_status(False)
                score = score + 1
            j = j + 1

        i = 0
        while i < len(GroupBlock):
            if (GroupBlock[i].status is False):
                pygame.draw.rect(dis, black, [GroupBlock[i].positionX, GroupBlock[i].positionY, squareWidth, squareHeight], 1)
            i = i + 1

        #barCollision!
        if(playerX <= 0 or playerX+200 >= width):
            changeX = 0

        if(vecY == playerY and
        vecX >= playerX and vecX <= playerX + 200):
            changeBy = -1
            changeBx = random.randint(-135, 135)/100
            print(changeBx)

        vecY = vecY + changeBy
        vecX = vecX + changeBx

        #wallCollisions!
        if (vecY == 0):
            changeBy = changeBy*-1
        if (vecX <= 0 or vecX >= width-1):
            changeBx = changeBx*-1

        if(vecY >= heigth):
            numBalls =  numBalls - 1
        
        #blockCollisions!
        x = 0
        while x < len(GroupBlock):
            if (GroupBlock[x].status is True):
                if(vecX >= GroupBlock[x].positionX 
                and vecX <= GroupBlock[x].positionX + squareWidth 
                and (vecY == GroupBlock[x].positionY + squareHeight
                or vecY == GroupBlock[x].positionY)):
                    changeBy = changeBy*-1

                if(vecY >= GroupBlock[x].positionY
                and vecY <= GroupBlock[x].positionY + squareHeight
                and (vecX == GroupBlock[x].positionX+ squareWidth
                or vecX == GroupBlock[x].positionX)):
                    changeBx = changeBx*-1
            x = x + 1

        #bar!
        pygame.draw.rect(dis, white, [playerX, playerY, 200, squareHeight], 3)
        pygame.draw.rect(dis, red, [playerX, playerY, 200, squareHeight])

        #ball!
        pygame.draw.rect(dis, white, [vecX, vecY, 3, 3], 1)

        #gameOver!
        if(numBalls <= 0):
            dis.fill(black)

            message3("You lost",red)

            message4("Press c to try again or q to quit.",red)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    gameover = True
                    quit()

                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        gameover = True
                        quit()
                    if event.key == pygame.K_c:
                        gameover = False
                        game()
        #win!
        if(score >= 50):
            dis.fill(black)

            message3("You won!",red)

            message4("Press c to try again or q to quit.",red)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    gameover = True
                    quit()

                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        gameover = True
                        quit()
                    if event.key == pygame.K_c:
                        gameover = False
                        game()

        #clock!
        clock = pygame.time.Clock() 
        clock.tick(speed)
        pygame.display.update()

        #initialPause!
        if score == -1 and numBalls != 0:
            time.sleep(2)
            score = score + 1

game()
pygame.quit()
quit()