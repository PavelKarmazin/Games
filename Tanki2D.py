import pygame
import random
import sys
pygame.init()

sc = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Танки")
pygame.display.flip()

L4 = [3, 4, 5, 6, 7, 8]
L3 = [1, 2, 3, 4, 5, 6, 7]
L2 = [1, 2, 3, 4, 5, 6, 7]
L1 = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11]
gunX = 0
gunY = 0
goUP = False
goDW = False
goRT = False
goLT = False

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            break
    for i in L1:
        sc.blit(block, [i*100,100])
    for i in L2:
        if i == 1:
            sc.blit(block, [400,100])
        else:
            sc.blit(block, [400,i*100-23*i])
    for i in L3:
        if i == 1:
            sc.blit(block, [700,100])
        else:
            sc.blit(block, [700,i*100-23*i])
    for i in L4:
        sc.blit(block, [i*100,900-20*9])

    sc.blit(block, [800,400-23*4])
    sc.blit(block, [900,400-23*4])
    sc.blit(block, [800,700-23*7])
    sc.blit(block, [900,700-23*7])

    sc.blit(block, [300,400-23*4])
    sc.blit(block, [200,400-23*4])
    sc.blit(block, [300,700-23*7])
    sc.blit(block, [200,700-23*7])

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
        if y>0:
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



        