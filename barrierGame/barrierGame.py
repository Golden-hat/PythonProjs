import numpy
import pygame
import time
import random

pygame.init();

#variables!--------
height = 400
width = 400

x1 = 200
y1 = 300

x1_change = 0       
y1_change = 0

gameover = False

#canvas!
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodge the walls!")

#gameloop!

def gameloop():
    while not gameover:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver = True;

    pygame.display.update() 

#termination--------
pygame.quit()
quit()
