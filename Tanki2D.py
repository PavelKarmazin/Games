import pygame
import random
import sys
pygame.init()
sc = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Танки")
pygame.display.flip()
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255, 255, 0)
def game():
    ### списки содержат числа для генерации блоков по оси Х
    y0, y1, y2, y3, y4, y5, y6, y7, y8 = 0, 100, 200, 300, 400, 500, 600, 700, 800 #высоты карты для создания блоков
    Ltanks = []
    L8 = []
    L7 = [0, 100, 200, 300, 400, 700, 800, 900, 1000, 1100]
    L6 = [400, 700]
    L5 = [200, 300, 400, 700, 800, 900]
    L4 = []
    L3 = [200, 300, 400, 700, 800, 900]
    L2 = [400, 700]
    L1 = [0, 100, 200, 300, 400, 700, 800, 900, 1000, 1100]
    L0 = []
    goUP = False
    goDW = False
    goRT = False
    goLT = False

    gunCount = 0 ### перезарядка оружия

    upStop = False
    dwStop = False
    rtStop = False
    ltStop = False
    #активация стопа при встрече с препятсвиями
    ltlt = False
    rtrt = False
    # вспомогают в def

    #стандартные цвета
    corXU, corXD, corXL, corXR = [], [], [], []
    corYU, corYD, corYL, corYR = [], [], [], []
    copyU, copyD, copyL, copyR = [], [], [], []
    # списки с координатами снарядов
    clock = pygame.time.Clock()
    fps = clock.tick(30)

    x = 550
    y = 800
    tankUp = True
    tankR = False
    tankL = False
    tankD = False
    ### переменные go содержат текущее нарпавление танка в виде bool
    game_over = False
    provk1 = False
    provk2 = False
    block = pygame.image.load(r'F:\PyGame\png\block.png')
    tank = pygame.image.load(r'F:\PyGame\png\tank.png')
    tank1 = pygame.image.load(r'F:\PyGame\png\tank1.png')
    tank2 = pygame.image.load(r'F:\PyGame\png\tank2.png')
    tank3 = pygame.image.load(r'F:\PyGame\png\tank3.png')
    snaryad = pygame.image.load(r'F:\PyGame\png\snaryad.png')
    snaryadR = pygame.image.load(r'F:\PyGame\png\snaryadR.png')
    snaryadD = pygame.image.load(r'F:\PyGame\png\snaryadD.png')
    snaryadL = pygame.image.load(r'F:\PyGame\png\snaryadL.png')
    tankVU = pygame.image.load(r'F:\PyGame\png\tankVragUp.png')
    tankVD = pygame.image.load(r'F:\PyGame\png\tankVragDw.png')
    tankVR = pygame.image.load(r'F:\PyGame\png\tankVragRg.png')
    tankVL = pygame.image.load(r'F:\PyGame\png\tankVragLt.png')
    VRX = 0
    VRY = 0
    vkl1 = False

    def boom(I, Y, l, a):
        global provk1, provk2
        if a<100:
            a = "0"
        elif a>1000:
            a = str(a)
            a = a[:2]
        else:
            a = str(a)
            a = a[0]
        if I==Y+33 or I==Y+34 or I==Y+35 or I==Y+36:
            provk1 = True
        else:
            provk1 = False
        if int(a) in l:
            provk2 = True
        else:
            provk2 = False
        if provk1 and provk2:
            l.remove(int(a))
            return True
    # это был выстрел вверх/вниз 
    def boom1(I, Y, l, a):
        global provk1, provk2
        if I in range(Y, Y+100) or I+14 in range(Y, Y+100):
            provk1 = True
        else:
            provk1 = False
        if a<100:
            a = "0"
        elif a>1000:
            a = str(a)
            a = a[:2]
        else:
            a = str(a)
            a = a[0]
        if int(a) in l:
            provk2 = True
        else:
            provk2 = False
        if provk1 and provk2:
            l.remove(int(a))
            return True
    # выстрел в лево

    def boom2(I, Y, l, a):
        global provk1, provk2
        if I in range(Y, Y+95) or I+14 in range(Y, Y+95):
            provk1 = True
        else:
            provk1 = False
        a = a-40
        if a<100:
            a = "0"
        elif a>1000:
            a = str(a)
            a = a[:2]
        else:
            a = str(a)
            a = a[0]
        if int(a)+1 in l:
            provk2 = True
        else:
            provk2 = False
        if provk1 and provk2:
            l.remove(int(a)+1)
            return True
    # выстрел в право

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
        if y in range(Y, Y+97):
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
        if y+100 in range(Y, Y+97):
            prov2 = True
        else:
            prov2 = False
        if prov1 and prov2:
            stop = True
        else:
            stop = False
        return stop

    def nazvanie3(stop, Y, l, Y1, X):
        if Y1 in range(Y, Y+97) or Y1+100 in range(Y, Y+100):
            prov1 = True
        else:
            prov1 = False
        if X<100:
            a = "0"
        elif X>1000:
            a = str(X)
            a = a[:2]
        else:
            a = str(X)
            a = a[0]
        if int(a) in l:
            prov2 = True
        else:
            prov2 = False
        if prov1 and prov2:
            stop = True
        else:
            stop = False  
        return stop

    def nazvanie4(stop, Y, l):
        if y in range(Y, Y+97) or y+100 in range(Y, Y+100):
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
        else:
            stop = False    
        return stop
    ### эти 4 функции это стоп танк, проверяют на препятсвия
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
        if not vkl1:
            sc.blit(tankVR, [VRX, VRY])
        else:
            sc.blit(tankVL, [VRX, VRY])
        for i in L1:
            sc.blit(block, [i, y1])
        for i in L2:
            sc.blit(block, [i, y2])
        for i in L3:
            sc.blit(block, [i, y3])
        for i in L4:
            sc.blit(block, [i,y4])
        for i in L5:
            sc.blit(block, [i,y5])
        for i in L6:
            sc.blit(block, [i,y6])
        for i in L7:
            sc.blit(block, [i,y7])
        for i in L8:
            sc.blit(block, [i,y8])
        # генерация по спискам Л и высотам У
        upStop = False
        if y in range(y0, y2+1):
                if nazvanie(upStop, y1, L1) or nazvanie(upStop, y2, L2):
                    upStop = True
        if y in range(y2, y4+1):
                if nazvanie(upStop, y3, L3) or nazvanie(upStop, y4, L4):
                    upStop = True
        if y in range(y4, y6+1):
                if nazvanie(upStop, y5, L5) or nazvanie(upStop, y6, L6):
                    upStop = True
        if y in range(y6, 901):
                if nazvanie(upStop, y7, L7) or nazvanie(upStop, y8, L8):
                    upStop = True
        # в зависимости от положения танка проверяю на препяствия
        

        dwStop = False
        if y in range(y0, y2+1):
                if nazvanie2(dwStop, y1, L1) or nazvanie2(dwStop, y2, L2):
                    dwStop = True
        if y in range(y2, y4+1):
                if nazvanie2(dwStop, y3, L3) or nazvanie2(dwStop, y4, L4):
                    dwStop = True
        if y in range(y4, y6+1):
                if nazvanie2(dwStop, y5, L5) or nazvanie2(dwStop, y6, L6):
                    dwStop = True
        if y in range(y6, 901):
                if nazvanie2(dwStop, y7, L7) or nazvanie2(dwStop, y8, L8):
                    dwStop = True
            

        ltStop = False
        if y in range(y0, y2+1):
                if nazvanie3(ltStop, y1, L1, y, x) or nazvanie3(ltStop, y2, L2, y, x):
                    ltStop = True
        if y in range(y2, y4+1):
                if nazvanie3(ltStop, y3, L3, y, x) or nazvanie3(ltStop, y4, L4, y, x):
                    ltStop = True
        if y in range(y4, y6+1):
                if nazvanie3(ltStop, y5, L5, y, x) or nazvanie3(ltStop, y6, L6, y, x):
                    ltStop = True
        if y in range(y6, 901):
                if nazvanie3(ltStop, y7, L7, y, x) or nazvanie3(ltStop, y8, L8, y, x):
                    ltStop = True
            

        rtStop = False
        if y in range(y0, y2+1):
                if nazvanie4(rtStop, y1, L1) or nazvanie4(rtStop, y2, L2):
                    rtStop = True
        if y in range(y2, y4+1):
                if nazvanie4(rtStop, y3, L3) or nazvanie4(rtStop, y4, L4):
                    rtStop = True
        if y in range(y4, y6+1):
                if nazvanie4(rtStop, y5, L5) or nazvanie4(rtStop, y6, L6):
                    rtStop = True
        if y in range(y6, 901):
                if nazvanie4(rtStop, y7, L7) or nazvanie4(rtStop, y8, L8):
                    rtStop = True


        keys = pygame.key.get_pressed()
        if tankUp:
            sc.blit(tank, [x, y])# если танк прямо то рисуем соответстующий
            if keys[pygame.K_SPACE]:
                if gunCount >= 40:
                    gunCount = 0
                    corXU.append(x+42)# добавляем в список координат снарядов соответстующие значения, которые позже отрисуем
                    corYU.append(y)
    
        elif tankR:
            sc.blit(tank1, [x, y])
            if keys[pygame.K_SPACE]:
                if gunCount >= 40:
                    gunCount = 0
                    corXR.append(x+100)
                    corYR.append(y+42)
        elif tankD:
            sc.blit(tank2, [x, y])
            if keys[pygame.K_SPACE]:
                if gunCount >= 40:
                    gunCount = 0
                    corXD.append(x+42)
                    corYD.append(y+100)
        elif tankL:
            sc.blit(tank3, [x, y])
            if keys[pygame.K_SPACE]:
                if gunCount >= 40:
                    gunCount = 0
                    corXL.append(x-45)
                    corYL.append(y+42)

        if keys[pygame.K_LEFT]:
            if x>0 and not ltStop:
                x -= 2 # нажал на лево - едешь на лево
                tankUp, tankR, tankL, tankD = False, False, True, False
#            if upStop:
 #               y += 2
  #          if dwStop:
   #             y -= 2
        if keys[pygame.K_RIGHT]:
            if x<1110 and not rtStop:
                x += 2
                tankUp, tankR, tankL, tankD = False, True, False, False
    #        if upStop:
     #           y += 2
      #      if dwStop:
       #         y -= 2
        if keys[pygame.K_UP]:
            if y>0 and not upStop:
                y -= 2
                tankUp, tankR, tankL, tankD = True, False, False, False
 #           if ltStop:
  #              x += 2
   #         if rtStop:
    #            x -= 2
        if keys[pygame.K_DOWN]:
            if y<800 and not dwStop:
                y += 2
                tankUp, tankR, tankL, tankD = False, False, False, True
     #       if ltStop:
      #          x += 2
       #     if rtStop:
        #        x -= 2
        Ltanks.append(x//100)
        Ltanks.append(VRX//100)

        for i, j in enumerate(corYU): # магия, это не эльфийский
            sc.blit(snaryad, [corXU[i], j]) # берем список со снарядами которые летят вверх и рисуем все эти снаряды
            if boom(j, y1, L1, corXU[i]) or boom(j, y2, L2, corXU[i]) or boom(j, y3, L3, corXU[i]) or boom(j, y4, L4, corXU[i]) or boom(j, y5, L5, corXU[i]) or boom(j, y6, L6, corXU[i]) or boom(j, y7, L7, corXU[i]) or boom(j, y8, L8, corXU[i]) or boom(j, y0, L0, corXU[i]):
                corYU.pop(i)
                corXU.pop(i) # если снаряд врезался в один из блоков, то удаляем этот снаряд из списков 
        for j in corYU:
            copyU.append(j-4)
        corYU = []
        corYU = copyU.copy()
        copyU.clear()## смещаем все снаряды которые летят вверх на 4 пикселя, это их скорость
        for d, i in enumerate(corYU):
            if i > 0:
                copyU.append(i)
            else:
                corXU.pop(d)
        corYU.clear()
        corYU = copyU.copy()
        copyU.clear()
        # перезапись всех снарядов, те что улетели вверх за границу карты не перезаписываем

        ### 

        for i, j in enumerate(corYD): # аналогично с верхом
            sc.blit(snaryadD, [corXD[i], j])
            if boom(j, y1, L1, corXD[i]) or boom(j, y2, L2, corXD[i]) or boom(j, y3, L3, corXD[i]) or boom(j, y4, L4, corXD[i]) or boom(j, y5, L5, corXD[i]) or boom(j, y6, L6, corXD[i]) or boom(j, y7, L7, corXD[i]) or boom(j, y8, L8, corXD[i]) or boom(j, y0, L0, corXD[i]):
                corYD.pop(i)
                corXD.pop(i) 
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
            if boom1(j, y1, L1, corXL[i]) or boom1(j, y2, L2, corXL[i]) or boom1(j, y3, L3, corXL[i]) or boom1(j, y4, L4, corXL[i]) or boom1(j, y5, L5, corXL[i]) or boom1(j, y6, L6, corXL[i]) or boom1(j, y7, L7, corXL[i]) or boom1(j, y8, L8, corXL[i]) or boom1(j, y0, L0, corXL[i]):
                corYL.pop(i)
                corXL.pop(i) 
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
            if boom2(j, y1, L1, corXR[i]) or boom2(j, y2, L2, corXR[i]) or boom2(j, y3, L3, corXR[i]) or boom2(j, y4, L4, corXR[i]) or boom2(j, y5, L5, corXR[i]) or boom2(j, y6, L6, corXR[i]) or boom2(j, y7, L7, corXR[i]) or boom2(j, y8, L8, corXR[i]) or boom2(j, y0, L0, corXR[i]):
                corYR.pop(i)
                corXR.pop(i) 
        for j in corXR:
            copyR.append(j+4)
            corXR = []
            corXR = copyR.copy()
            copyR.clear()
        for d, i in enumerate(corXR):
            if i < 1200:
                copyR.append(i)
            else:
                corYR.pop(d)
        corXR = copyR.copy()
        copyR.clear()

        if VRX >= 500:
            vkl1 = True
            sc.blit(tankVD, [500, 0])
            corXD.append(535)
            corYD.append(100)
        if VRX < 0:
            vkl1 = False
        if vkl1:
            VRX-=2
        else:
            VRX+=2
        if x//100 not in Ltanks:
            game_over = True
        if game_over:
            sc.fill(BLACK)
            menu()
        Ltanks.clear()

        pygame.display.update()
        sc.fill(BLACK)
        gunCount += 1 # счёт перезарядки

def menu():
    pygame.draw.rect(sc, GREEN, (500, 200, 225, 45))
    font = pygame.font.SysFont('stxingkai', 35)
    text1 = font.render("Играть", True, RED)
    text_rect = text1.get_rect()
    text_x = 570
    text_y = 210
    sc.blit(text1, [text_x, text_y])

    pygame.draw.rect(sc, GREEN, (500, 500, 225, 45))
    font = pygame.font.SysFont('stxingkai', 35)
    text1 = font.render("Выйти", True, RED)
    text_rect = text1.get_rect()
    text_x = 570
    text_y = 510
    sc.blit(text1, [text_x, text_y])
    
    pygame.display.update()
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
            ### проверка на нажатие кнокпи
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                if x_mouse > 500 and x_mouse < 725:
                    if y_mouse > 200 and y_mouse < 245:
                        game()
                    elif y_mouse > 500 and y_mouse < 545:
                        pygame.quit()
                        sys.exit(0)
menu()        