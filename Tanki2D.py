import pygame
import random
import sys
pygame.init()

sc = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Танки")
pygame.display.flip()
L8 = [4, 7]
y8 = 600-23*6
L7 = [4, 7]
y7 = 500-23*5
L6 = [2, 3, 4, 7, 8, 9]
y6 = 700-23*7
L5 = [2, 3, 4, 7, 8, 9]
y5 = 400-23*4
L4 = [3, 4, 5, 6, 7, 8]
y4 = 900-20*9
L3 = [4, 7]
y3 = 300-23*3
L2 = [4, 7]
y2 = 200-23*2
L1 = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11]
y1 = 100
#### y это высота для блоков кирпичей в определенной стене
gunX = 0
gunY = 0
goUP = False
goDW = False
goRT = False
goLT = False

upStop = False
dwStop = False
rtStop = False
ltStop = False

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255, 255, 0)
x = 550
y = 800
tankUp = True
tankR = False
tankL = False
tankD = False
game_over = False
block = pygame.image.load(r'F:\PyGame\png\block.png')
tank = pygame.image.load(r'F:\PyGame\png\tank.png')
tank1 = pygame.image.load(r'F:\PyGame\png\tank1.png')
tank2 = pygame.image.load(r'F:\PyGame\png\tank2.png')
tank3 = pygame.image.load(r'F:\PyGame\png\tank3.png')
def nazvanie(stop, Y, l):
    if x<100:
        a = "0"
    elif x>1000:
        a = str(x)
        a = a[:2]
    else:
        a = str(x)
        a = a[0]
    if int(a) in l or int(a)+1 in l:
        prov1 = True
    else:
        prov1 = False
    if y in range(Y, Y+77):
        prov2 = True
    else:
        prov2 = False
    if prov1 and prov2:
        stop = True
    else:
        stop = False
    return stop 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            break
    for i in L1:
        sc.blit(block, [i*100, y1])
    for i in L2:
        sc.blit(block, [i*100, y2])
    for i in L3:
        sc.blit(block, [i*100, y3])
    for i in L4:
        sc.blit(block, [i*100,y4])
    for i in L5:
        sc.blit(block, [i*100,y5])
    for i in L6:
        sc.blit(block, [i*100,y6])
    for i in L7:
        sc.blit(block, [i*100,y7])
    for i in L8:
        sc.blit(block, [i*100,y8])
    if nazvanie(upStop, y1, L1) or nazvanie(upStop, y2, L2) or nazvanie(upStop, y3, L3) or nazvanie(upStop, y4, L4) or nazvanie(upStop, y5, L5) or nazvanie(upStop, y6, L6) or nazvanie(upStop, y7, L7) or nazvanie(upStop, y8, L8):
        upStop = True
    else:
        upStop = False

    keys = pygame.key.get_pressed()
    if tankUp:
        sc.blit(tank, [x, y])
        if keys[pygame.K_SPACE]:
            goUP = True
            goDW, goLT, goRT = False, False, False
            gunX = x+50
            gunY = y
    elif tankR:
        sc.blit(tank1, [x, y])
        if keys[pygame.K_SPACE]:
            goRT = True
            goDW, goLT, goUP = False, False, False
            gunX = x+100
            gunY = y+50
    elif tankD:
        sc.blit(tank2, [x, y])
        if keys[pygame.K_SPACE]:
            goDW = True
            goUP, goLT, goRT = False, False, False
            gunX = x+50
            gunY = y+100
    elif tankL:
        sc.blit(tank3, [x, y])
        if keys[pygame.K_SPACE]:
            goLT = True
            goDW, goUP, goRT = False, False, False
            gunX = x
            gunY = y+50

    if keys[pygame.K_LEFT]:
        if x>0:
            x -= 5
            tankUp, tankR, tankL, tankD = False, False, True, False
    if keys[pygame.K_RIGHT]:
        if x<1110:
            x += 5
            tankUp, tankR, tankL, tankD = False, True, False, False
    if keys[pygame.K_UP]:
        if y>0 and not upStop:
            y -= 5
            tankUp, tankR, tankL, tankD = True, False, False, False
    if keys[pygame.K_DOWN]:
        if y<800:
            y += 5
            tankUp, tankR, tankL, tankD = False, False, False, True
    if goUP:
        pygame.draw.circle(sc, YELLOW, (gunX, gunY), 15)
        gunY -= 5
    elif goRT:
        pygame.draw.circle(sc, YELLOW, (gunX, gunY), 15)
        gunX += 5
    elif goDW:
        pygame.draw.circle(sc, YELLOW, (gunX, gunY), 15)
        gunY += 5
    elif goLT:
        pygame.draw.circle(sc, YELLOW, (gunX, gunY), 15)
        gunX -= 5


    pygame.display.update()
    sc.fill(BLACK)



        