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

gunCount = 0

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
corXU, corXD, corXL, corXR = [], [], [], []
corYU, corYD, corYL, corYR = [], [], [], []
copyU, copyD, copyL, copyR = [], [], [], []

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
snaryad = pygame.image.load(r'F:\PyGame\png\snaryad.png')
snaryadR = pygame.image.load(r'F:\PyGame\png\snaryadR.png')
snaryadD = pygame.image.load(r'F:\PyGame\png\snaryadD.png')
snaryadL = pygame.image.load(r'F:\PyGame\png\snaryadL.png')
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

def nazvanie2(stop, Y, l):
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
    if y+100 in range(Y, Y+75):
        prov2 = True
    else:
        prov2 = False
    if prov1 and prov2:
        stop = True
    else:
        stop = False
    return stop

def nazvanie3(stop, Y, l):
    global x
    if y in range(Y, Y+75) or y+75 in range(Y, Y+75):
        prov1 = True
    else:
        prov1 = False
    if x<100:
        a = "0"
    elif x>1000:
        a = str(x)
        a = a[:2]
    else:
        a = str(x)
        a = a[0]
    if int(a) in l:
        prov2 = True
    else:
        prov2 = False
    if prov1 and prov2:
        stop = True
        x+=1
    else:
        stop = False    
    return stop

def nazvanie4(stop, Y, l):
    global x
    if y in range(Y, Y+75) or y+75 in range(Y, Y+75):
        prov1 = True
    else:
        prov1 = False
    if x<100:
        a = "0"
    elif x>1000:
        a = str(x)
        a = a[:2]
    else:
        a = str(x)
        a = a[0]
    if int(a)+1 in l:
        prov2 = True
    else:
        prov2 = False
    if prov1 and prov2:
        stop = True
        x-=1
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
    if nazvanie2(dwStop, y1, L1) or nazvanie2(dwStop, y2, L2) or nazvanie2(dwStop, y3, L3) or nazvanie2(dwStop, y4, L4) or nazvanie2(dwStop, y5, L5) or nazvanie2(dwStop, y6, L6) or nazvanie2(dwStop, y7, L7) or nazvanie2(dwStop, y8, L8):
        dwStop = True
    else:
        dwStop = False
    if nazvanie3(ltStop, y1, L1) or nazvanie3(ltStop, y2, L2) or nazvanie3(ltStop, y3, L3) or nazvanie3(ltStop, y4, L4) or nazvanie3(ltStop, y5, L5) or nazvanie3(ltStop, y6, L6) or nazvanie3(ltStop, y7, L7) or nazvanie3(ltStop, y8, L8):
        ltStop = True
    else:
        ltStop = False
    if nazvanie4(rtStop, y1, L1) or nazvanie4(rtStop, y2, L2) or nazvanie4(rtStop, y3, L3) or nazvanie4(rtStop, y4, L4) or nazvanie4(rtStop, y5, L5) or nazvanie4(rtStop, y6, L6) or nazvanie4(rtStop, y7, L7) or nazvanie4(rtStop, y8, L8):
        rtStop = True
    else:
        rtStop = False



    keys = pygame.key.get_pressed()
    if tankUp:
        sc.blit(tank, [x, y])
        if keys[pygame.K_SPACE]:
            if gunCount >= 40:
                gunCount = 0
                corXU.append(x+25)
                corYU.append(y-45)
    elif tankR:
        sc.blit(tank1, [x, y])
        if keys[pygame.K_SPACE]:
            if gunCount >= 40:
                gunCount = 0
                corXR.append(x+100)
                corYR.append(y+25)
    elif tankD:
        sc.blit(tank2, [x, y])
        if keys[pygame.K_SPACE]:
            if gunCount >= 40:
                gunCount = 0
                corXD.append(x+25)
                corYD.append(y+100)
    elif tankL:
        sc.blit(tank3, [x, y])
        if keys[pygame.K_SPACE]:
            if gunCount >= 40:
                gunCount = 0
                corXL.append(x-45)
                corYL.append(y+25)

    if keys[pygame.K_LEFT]:
        if x>0 and not ltStop:
            x -= 3
            tankUp, tankR, tankL, tankD = False, False, True, False
    if keys[pygame.K_RIGHT]:
        if x<1110 and not rtStop:
            x += 3
            tankUp, tankR, tankL, tankD = False, True, False, False
    if keys[pygame.K_UP]:
        if y>0 and not upStop:
            y -= 3
            tankUp, tankR, tankL, tankD = True, False, False, False
    if keys[pygame.K_DOWN]:
        if y<800 and not dwStop:
            y += 3
            tankUp, tankR, tankL, tankD = False, False, False, True

    for i, j in enumerate(corYU):
        sc.blit(snaryad, [corXU[i], j])
    for j in corYU:
        copyU.append(j-4)
    corYU = []
    corYU = copyU.copy()
    copyU.clear()
    for d, i in enumerate(corYU):
        if i > 0:
            copyU.append(i)
        else:
            corXU.pop(d)
    corYU.clear()
    corYU = copyU.copy()
    copyU.clear()

    ###

    for i, j in enumerate(corYD):
        sc.blit(snaryadD, [corXD[i], j])
    for j in corYD:
        copyD.append(j+4)
    corYD = []
    corYD = copyD.copy()
    copyD.clear()
    for d, i in enumerate(corYD):
        if i < 1200:
            copyD.append(i)
        else:
            corXD.pop(d)
    corYD.clear()
    corYD = copyD.copy()
    copyD.clear()

    ###

    for i, j in enumerate(corYL):
        sc.blit(snaryadL, [corXL[i], j])
    for j in corXL:
        copyL.append(j-4)
    corXL = []
    corXL = copyL.copy()
    copyL.clear()
    for d, i in enumerate(corXL):
        if i > 0:
            copyL.append(i)
        else:
            corYL.pop(d)
    corXL.clear()
    corXL = copyL.copy()
    copyL.clear()

    ###

    for i, j in enumerate(corYR):
        sc.blit(snaryadR, [corXR[i], j])
    for j in corXR:
        copyR.append(j+4)
    corXR = []
    corXR = copyR.copy()
    copyR.clear()
    for d, i in enumerate(corXR):
        if i > 0:
            copyR.append(i)
        else:
            corYR.pop(d)
    corXR.clear()
    corXR = copyR.copy()
    copyR.clear()


    pygame.display.update()
    sc.fill(BLACK)
    pygame.time.delay(1)
    gunCount += 1


        