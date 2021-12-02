import pygame
import time
import random
from pygame.constants import WINDOWRESIZED

pygame.init();

#dimensions!-------------------------------------------------------------------
height = 600;
width = 800;

x1 = 400
y1 = 300
 
x1_change = 0       
y1_change = 0

snakespeed = 15
score = 0

#canvas!----------------------------------------------------------------------
dis = pygame.display.set_mode((width, height));
pygame.display.set_caption('Snake!');

#fruit 1st!-------------------------------------------------------------------
randvaluex = round(random.randrange(0, width - 20) / 20.0) * 20.0
randvaluey = round(random.randrange(0, height - 20) / 20.0) * 20.0

#snakegrowth and drawing!-----------------------------------------------------
LenSnake = 1
snake_list = []
def snake_body(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snakebodycolor, [x[0], x[1], 20, 20])

#colors!-----------------------------------------------------------------------
red=(255,0,0)
snakebodycolor = (127,255,0)
black = (0, 0, 0)
font_style = pygame.font.SysFont(None, 30)

#endgameLogic!----------------------------------------------------------------
gameOver = False;
while not gameOver:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOver = True;

    #Movement!----------------------------------------------------------------
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x1_change = 20;
                y1_change = 0;

            elif event.key==pygame.K_LEFT:
                x1_change = -20;
                y1_change = 0;

            elif event.key==pygame.K_DOWN:
                x1_change = 0;
                y1_change = 20;

            elif event.key==pygame.K_UP:
                x1_change = 0;
                y1_change = -20;
                
    x1 += x1_change;
    y1 += y1_change;

    #fruit!-------------------------------------------------------------------
    if randvaluex == x1 and randvaluey == y1:
        randvaluex = round(random.randrange(20, width - 40) / 20.0) * 20.0
        randvaluey = round(random.randrange(20, height - 40) / 20.0) * 20.0
        score += 1
        LenSnake += 1
        print(score)
        print("Yummy!")

    if (x1 > width or y1 >= height) or (y1 < 0 or x1 < 0):
        gameOver = True;

    #painting!----------------------------------------------------------------
    dis.fill(black)
    pygame.draw.rect(dis, red, [randvaluex, randvaluey, 20, 20])

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_list.append(snake_Head)
    
    if len(snake_list) > LenSnake:
       del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_Head:
            gameOver = True

    print(len(snake_list))

    snake_body(snake_list)

    def message(msg,color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [width/50, height/50])

    message("Score: "+str(score),snakebodycolor);
    pygame.display.update()

    #clock!-------------------------------------------------------------------
    clock = pygame.time.Clock() 
    clock.tick(snakespeed)

    pygame.display.update() 

#you lost!--------------------------------------------------------------------
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width/2, height/2])

message("You lost",red)
pygame.display.update()
time.sleep(2)


#termination!
pygame.quit();
quit(); 

