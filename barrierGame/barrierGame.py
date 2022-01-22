import numpy as np
from numpy.random.mtrand import rand
import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, TIMER_RESOLUTION, K_a, K_c, K_d, K_s, K_w

pygame.init();

#variables!
height = 800
width = 1000

font_style = pygame.font.SysFont(None, 30)
font_style2= pygame.font.SysFont(None, 80)
score = 0
diff = 0
SpawnDisty = []

#colors!
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (154,205,50)

#canvas!
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodge the walls!")

#wall generation!
def wall (SpawnDisty, type, WallArray):
    i = 0
    while i < len(WallArray):
        pygame.draw.rect(dis, yellow, [WallArray[i], SpawnDisty[type], 100, 10])
        i += 1

def randy(type):
    if SpawnDisty[type]>= height:
        rval = np.random.randint(0, 10, 10)
    return rval

#player!
def player(x1p, y1p):
    pygame.draw.rect(dis, red, [x1p, y1p, 10, 10])

#gameloop!
def gameloop(score, diff):

    x1_change = 0
    y1_change = 0
    gameOver = False
    gameClose = False
    SpawnDisty = [0, -200, -400, -600]

    iter1 = 0
    iter2 = 0
    iter3 = 0
    iter4 = 0

    gamespeed = 15
    x1 = width/2
    y1 = height/2
    
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0

    while not gameOver:
        
        while z1 < iter1+1:
            rval1 = np.random.randint(0, 10, 10)
            z1 += 1
        while z2 < iter2+1:
            rval2 = np.random.randint(0, 10, 10)
            z2 += 1
        while z3 < iter3+1:
            rval3 = np.random.randint(0, 10, 10)
            z3 += 1
        while z4 < iter4+1:
            rval4 = np.random.randint(0, 10, 10)
            z4 += 1

        #walls!
        WallArray1 = [rval1[0]*100, rval1[1]*100, rval1[2]*100, 
        rval1[3]*100, rval1[4]*100, rval1[1]*100, rval1[6]*100, 
        rval1[7]*100, rval1[8]*100, rval1[1]*100]

        WallArray2 = [rval2[0]*100, rval2[1]*100, rval2[2]*100, 
        rval2[3]*100, rval2[4]*100, rval2[5]*100, rval2[6]*100, 
        rval2[7]*100, rval2[8]*100, rval2[1]*100]
        
        WallArray3 = [rval3[0]*100, rval3[1]*100, rval3[2]*100, 
        rval3[1]*100, rval3[4]*100, rval3[5]*100, rval3[6]*100, 
        rval3[7]*100, rval3[8]*100, rval3[9]*100]

        WallArray4 = [rval4[0]*100, rval4[1]*100, rval4[2]*100, 
        rval4[3]*100, rval4[4]*100, rval4[5]*100, rval4[1]*100, 
        rval4[7]*100, rval4[8]*100, rval4[9]*100]

        #GameOverLogic!
        while gameClose == True:
                def message(msg,color):
                    mesg = font_style2.render(msg, True, color)
                    dis.blit(mesg, [width/2.5, height/2.25])

                message("You lost",red)

                def message3(msg,color):
                    mesg = font_style.render(msg, True, color)
                    dis.blit(mesg, [width/2.5 + 200, height/2.25 +200])

                message3("Press c to try again or q to quit",red)

                pygame.display.update()

                for event in pygame.event.get():

                    if event.type==pygame.QUIT:
                        gameOver = True
                        gameClose = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameOver = True
                            gameClose = False
                        if event.key == pygame.K_c:
                            gameOver = False
                            SpawnDisty = [0, -200, -400, -600]
                            score = 0
                            gameloop(score, diff)
               

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                gameOver = True 

            if event.type==pygame.KEYDOWN:
                if event.key == K_w:
                    y1_change = -10;
                    x1_change = 0;
                elif event.key == K_s:
                    y1_change = 20;
                    x1_change = 0;
                elif event.key == K_a:
                    y1_change = 0;
                    x1_change = -15;
                elif event.key == K_d:
                    y1_change = 0;
                    x1_change = 15;
                    
        x1 += x1_change
        y1 += y1_change 

        #collisions!
        j = 0
        while j < len(WallArray1): 

            if (x1 >= WallArray1[j] 
            and x1 < WallArray1[j]+100
            and (y1 == SpawnDisty[0]+20 or y1 == SpawnDisty[0]+10)):
                gameClose = True

            if (x1 >= WallArray2[j] 
            and x1 < WallArray2[j]+100
            and (y1 == SpawnDisty[1]+20 or y1 == SpawnDisty[1]+10)):
                gameClose = True

            if (x1 >= WallArray3[j] 
            and x1 < WallArray3[j]+100
            and (y1 == SpawnDisty[2]+20 or y1 == SpawnDisty[2]+10)):
                gameClose = True
            
            if (x1 >= WallArray4[j] 
            and x1 < WallArray4[j]+100
            and (y1 == SpawnDisty[3]+20 or y1 == SpawnDisty[3]+10)):
                gameClose = True
            j += 1

            if (x1 > width or y1 >= height) or (y1 < 0 or x1 < 0):
                gameClose = True
        
        #clock!
        clock = pygame.time.Clock() 
        clock.tick(gamespeed)

        i = 0
        while i < len(SpawnDisty):
            SpawnDisty[i] += 10
            i += 1
            
            if SpawnDisty[0]>= height:
                SpawnDisty[0] = 0
                score += 1
                diff += 1
                iter1 += 1
            if SpawnDisty[1]>= height:
                SpawnDisty[1] = 0
                score += 1
                diff += 1
                iter2 += 1
            if SpawnDisty[2]>= height:
                SpawnDisty[2] = 0
                score += 1
                diff += 1
                iter3 += 1
            if SpawnDisty[3]>= height:
                SpawnDisty[3] = 0 
                score += 1
                diff += 1
                iter4 += 1

        #difficulty
        if diff%11 == 10:
            gamespeed += 2
            diff += 1
        
        #drawing!
        dis.fill(black)
        player(x1, y1)

        wall(SpawnDisty, 0, WallArray1)
        wall(SpawnDisty, 1, WallArray2)
        wall(SpawnDisty, 2, WallArray3)
        wall(SpawnDisty, 3, WallArray4)

        def message(msg,color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [width/50, height/50])

        message("Score: "+str(score),red)

        pygame.display.update()

    #termination
    pygame.quit()
    quit()

gameloop(score, diff)