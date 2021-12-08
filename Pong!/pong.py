import pygame
import random
import time

from pygame import draw
from pygame.constants import K_DOWN, K_UP, KEYDOWN, K_q, K_s, K_w

pygame.init()

#Variables!
width = 1000
height = 800
gameclose = False
rectlen = 180
rounds = 5

score1 = 0
score2 = 0

randx = 10
randy = (random.randrange(-10, 10))

#Colors!
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)

#defs!

def drawPoint(coordx, coordy):
    pygame.draw.rect(dis, white, [coordx, coordy, 10, 10])

def drawRectPlayers(movX, movY):
    pygame.draw.rect(dis, white, [movX, movY, 10, rectlen])

def drawline():
    pygame.draw.line(dis, white, [width/2, 0], [width/2, height], 1)

font_style = pygame.font.SysFont(None, 30)
font_style2 = pygame.font.SysFont(None, 80)

def message(msg, color):
    mesg = font_style2.render(msg, True, color)
    dis.blit(mesg, [width/50 + 220, height/50])


def message2(msg, color):
    mesg = font_style2.render(msg, True, color)
    dis.blit(mesg, [width/50 + 720, height/50])

#canvas!
dis = pygame.display.set_mode((width, height))

#gameloop!
def gameloop(randx, randy, rounds, i, score1, score2):

    coordx = width/2
    coordy = height/2   
    signx = round(random.randint(-1, 1))
    signy = round(random.randint(-1, 1))
    print(signy)
    print(signx)
    diff = 0

    movy1 = 300
    movy2 = 300

    movy1_change = 0
    movy2_change = 0
    gamespeed = 40
    gameclose = True

    if i == rounds:
        gameclose = False

    while gameclose == False:

        dis.fill(black)
        def message3(msg,color):
                mesg = font_style2.render(msg, True, color)
                dis.blit(mesg, [width/2.5 -100, height/2.25])
        if score2 > score1:
            message3("Player 2 wins!",red)
        else:
            message3("Player 1 wins!",red)

        def message4(msg,color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [width/2.5 + 200, height/2.25 +200])

        message4("Press c to try again or q to quit" ,red)

        def message5(msg,color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [width/2.5 + 300, height/2.25 +300])

        message5("Score1: "+str(score1) + ", Score2: "+str(score2), red)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                gameclose = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameclose = True
                if event.key == pygame.K_c:
                    gameover = False
                    score1 = 0
                    score2 = 0
                    i = 0
                    gameloop(randx, randy, rounds, i, score1, score2)
    

    while i < rounds:

        gameover = False
        while not gameover:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    i = rounds
                
                if event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        movy2_change = -20
                    elif event.key == K_DOWN:
                        movy2_change = 20  
                    if event.key == K_w:
                        movy1_change = -20
                    elif event.key == K_s:
                        movy1_change = 20

                if event.type == pygame.KEYUP:
                    if event.key == K_UP:
                        movy2_change = 0
                    elif event.key == K_DOWN:
                        movy2_change = 0
                    if event.key == K_w:
                        movy1_change = 0
                    elif event.key == K_s:
                        movy1_change = 0

            movy1 += movy1_change
            movy2 += movy2_change

            #collision!
            if ((coordx == width-70) and (coordy >= movy2) 
            and (coordy <= (movy2 + rectlen))) or ((coordx == 60) 
            and (coordy >= movy1) and (coordy <= (movy1 + rectlen))):
                randy = (random.randrange(-10, 10))         
                signx *= -1
                print(randy)
                diff += 1

            coordx += randx*signx

            if coordy <= 0 or coordy >= height-10:
                signy *= -1   

            coordy += randy*signy
            
            if (coordx < 0 or coordx > width-10):

                if (coordx > width-10):
                    score1 += 1

                if (coordx < 0):
                    score2 += 1
    
                i += 1
                time.sleep(1)
                gameloop(randx, randy, rounds, i, score1, score2)

            #prevention!
            if signy == 0:
                signy = round(random.randint(-1, 1))
            if signx == 0:
                signx = round(random.randint(-1, 1))

            if movy1 <= 0:
                movy1 = 0
            if movy1 >= height-rectlen:
                movy1 = height-rectlen

            if movy2 <= 0:
                movy2 = 0
            if  movy2 >= height-rectlen:
                movy2 = height-rectlen

            #Drawing!
            dis.fill(black)
            drawPoint(coordx, coordy)

            drawRectPlayers(60, movy1)
            drawRectPlayers(width-70, movy2)
            drawline()

            message(str(score1), white)
            message2(str(score2), white)

            #difficulty
            if diff%6 == 5:
                gamespeed+= 5
                diff += 1

            #clock!
            clock = pygame.time.Clock() 
            clock.tick(gamespeed)

            pygame.display.update()

    pygame.quit()
    quit()        

gameloop(randx, randy, rounds, 0, score1, score2)




