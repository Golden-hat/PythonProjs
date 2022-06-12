import pygame
import time
import random

pygame.init()

#display/variables!
width = 1000
heigth = 800
dis = pygame.display.set_mode((width,heigth))
pygame.display.set_caption('Game of Life!')

#colors!
white = (255, 255, 255)
black = (0, 0, 0)

#variables!
displacementX = 0
displacementY = 0

#functions!
class cell:
    def __init__(self, posX, posY, stats):
        self.positionX = posX
        self.positionY = posY
        self.status = stats

    # status 0 = dead
    # status 1 = alive

    def set_status(self, x):
        self.status = x

cells = []

#position assignment!
j = 0
while j <= int(heigth/10):
    i = 0
    displacementX = 0
    while i < int(width/10):
        cells.append(cell(displacementX, displacementY, 0))
        displacementX = displacementX + 10
        i = i + 1
    displacementY = displacementY + 10
    j = j + 1

def gameloop():

    mousePosX = -10
    mousePosY = -10

    mousePosXDel = -10
    mousePosYDel = -10

    gameOver = False
    while not gameOver:

        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePosX = pygame.mouse.get_pos()[0]
                mousePosY = pygame.mouse.get_pos()[1]
        
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    mousePosXDel = pygame.mouse.get_pos()[0]
                    mousePosYDel = pygame.mouse.get_pos()[1]
                    print(mousePosXDel)

            if event.type==pygame.QUIT:
                gameOver = True

        #drawing!
        for i in range (0, int((width/10)*(heigth/10))):

            if cells[i].status == 0 and (mousePosX >= cells[i].positionX and mousePosX < cells[i].positionX + 10) and (mousePosY >= cells[i].positionY and mousePosY < cells[i].positionY + 10):
                cells[i].status = 1
                pygame.draw.rect(dis, white, [cells[i].positionX, cells[i].positionY, 10, 10])
                pygame.display.update()

            if cells[i].status == 1 and (mousePosXDel >= cells[i].positionX and mousePosXDel < cells[i].positionX + 10) and (mousePosYDel >= cells[i].positionY and mousePosYDel < cells[i].positionY + 10):
                cells[i].status = 0
                pygame.draw.rect(dis, black, [cells[i].positionX, cells[i].positionY, 10, 10])
                pygame.display.update()

         
gameloop()
pygame.quit()
quit()