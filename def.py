import pygame
import sys
import random
pygame.init()



#поле 
sc = pygame.display.set_mode((1048,745))
pygame.display.set_caption("монополия")
pygame.display.flip()
image = pygame.image.load('F:\PyGame/monopoly.jpg')
#списки значения которых перебираются в цикле while
color = [(225, 0, 50), (0, 255, 0), (128,128,128), (0, 255, 0)]
line = [1, 1, 1, 1]
a = [0, 0, 0, 0]
stop = [False, False, False, False]
Money = [15000, 15000, 15000, 15000,]
active = [[], [], [], []]
ruscolor = ['красный', 'синий', 'серый', 'зелёный']
#основные переменные
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0,0,0)
GREY = (128,128,128)
rand = 0
yes = 0
no = 0
game_over = False
query = 0

pygame.draw.rect(sc, WHITE, (748, 0, 300, 745))
# список координат
x11 = [675, 675, 675, 675]
x12 = [725, 725, 725, 725]
y1 = [685, 685, 685, 685]
y2 = [690, 690, 690, 690]
x21 = [695, 695, 695, 695]
x22 = [725, 725, 725, 725]

x1r1, x1r2, x1b1, x1b2, x1gy1, x1gy2, x1gn1, x1gn2 = 675, 725, 675, 725, 675, 725, 675, 725
yr1, yr2, yb1, yb2, ygy1, ygy2, ygn1, ygn2 = 685, 690, 685, 690, 685, 690, 685, 690
x2r1, x2r2, x2b1, x2b2, x2gy1, x2gy2, x2gn1, x2gn2 =  695, 725, 695, 725, 695, 725, 695, 725

sc.blit(image, [0,0])
pygame.display.update()
while True:
    pygame.draw.polygon(sc, RED, [[x11[0], x12[0]], [y1[0], y2[0]], [x21[0], x22[0]]])
    pygame.draw.polygon(sc, BLUE, [[x11[1], x12[1]], [y1[1], y2[1]], [x21[1], x22[1]]])
    pygame.draw.polygon(sc, GREY, [[x11[2], x12[2]], [y1[2], y2[2]], [x21[2], x22[2]]])
    pygame.draw.polygon(sc, GREEN, [[x11[3], x12[3]], [y1[3], y2[3]], [x21[3], x22[3]]])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            break
        elif not game_over:
            pygame.draw.rect(sc, WHITE, (295, 220, 140, 20))
            font = pygame.font.SysFont('stxingkai', 30)
            text1 = font.render("Кинуть кубик", True, BLACK)
            text_rect = text1.get_rect()
            text_x = 300
            text_y = 220
            sc.blit(text1, [text_x, text_y])
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                if x_mouse > 840 and x_mouse < 920 and y_mouse > 145 and y_mouse < 175:
                    yes = 1
                elif x_mouse > 935 and x_mouse < 1050 and y_mouse > 145 and y_mouse < 175:
                    no = 1
                if x_mouse > 295 and x_mouse < 435 and y_mouse > 220 and y_mouse < 240:
                    pygame.draw.rect(sc, WHITE, (345, 250, 30, 30))
                    rand = random.randint(1, 6)
                    if rand == 1:
                        pygame.draw.circle(sc, RED, (360, 265), 6)
                    elif rand == 2:
                        pygame.draw.circle(sc, BLACK, (355, 260), 4)
                        pygame.draw.circle(sc, BLACK, (365, 270), 4)
                    elif rand == 3:
                        pygame.draw.circle(sc, BLACK, (352, 257), 4)
                        pygame.draw.circle(sc, BLACK, (361, 266), 4)
                        pygame.draw.circle(sc, BLACK, (370, 274), 4)
                    elif rand == 4:
                        pygame.draw.circle(sc, RED, (353, 258), 4)
                        pygame.draw.circle(sc, RED, (353, 272), 4)
                        pygame.draw.circle(sc, RED, (367, 258), 4)
                        pygame.draw.circle(sc, RED, (367, 272), 4)
                    elif rand == 5:
                        pygame.draw.circle(sc, BLACK, (352, 257), 4)
                        pygame.draw.circle(sc, BLACK, (352, 274), 4)
                        pygame.draw.circle(sc, BLACK, (361, 266), 4)
                        pygame.draw.circle(sc, BLACK, (370, 257), 4)
                        pygame.draw.circle(sc, BLACK, (370, 274), 4)
                    elif rand == 6:
                        pygame.draw.circle(sc, BLACK, (351, 258), 4)
                        pygame.draw.circle(sc, BLACK, (351, 272), 4)
                        pygame.draw.circle(sc, BLACK, (368, 258), 4)
                        pygame.draw.circle(sc, BLACK, (368, 272), 4)
                        pygame.draw.circle(sc, BLACK, (360, 272), 4)
                        pygame.draw.circle(sc, BLACK, (360, 258), 4)
                    pygame.display.update()
                    pygame.draw.rect(sc, WHITE, (748, 0, 300, 745))                   
                    
                    if query == 4:
                        query = 0
                    i = query
                    if i == 0:
                        x, y, z = 1, 2, 3
                    elif i == 1:
                        x, y, z = 0, 2, 3
                    elif i == 2:
                        x, y, z = 0, 1, 3
                    elif i == 3:
                        x, y, z = 0, 1, 2
                    if stop[i] == True:
                        stop[i] = False
                    else:
                        a[i] = a[i] + rand
                        if a[i]<10 or a[i]>=40:
                            if a[i] >= 40:
                                a[i] = a[i] - 40
                                rand = a[i] 
                                line[i] = 1
                                x11[i], y1[i], x21[i] = 670, 680, 690
                            x12[i], y2[i], x22[i] = 725, 690, 725
                            x11[i], y1[i], x21[i], line[i] = x11[i] - 62*rand, y1[i] - 62*rand, x21[i] - 62*rand, 1
                        elif a[i]>=10 and a[i]<20:
                            if line[i] == 1:
                                rand = a[i] - 10
                                x12[i], y2[i], x22[i] = 695, 660, 695
                            x11[i], y1[i], x21[i] = 25, 35, 45
                            x12[i], y2[i], x22[i], line[i] = x12[i] - 62*rand, y2[i] - 62*rand, x22[i] - 62*rand, 2
                        elif a[i] >=20 and a[i]<30:
                            if line[i] == 2:
                                rand = a[i] - 20
                                x11[i], y1[i], x21[i] = 50, 60, 70
                            x12[i], y2[i], x22[i], line[i] = 60, 25, 60, 3
                            x11[i], y1[i], x21[i] = x11[i] + 62*rand, y1[i] + 62*rand, x21[i] + 62*rand
                        elif a[i] >= 30 and a[i]<40:
                            if line[i] == 3:
                                rand = a[i] - 30
                                x12[i], y2[i], x22[i] = 75, 40, 75
                            x11[i], y1[i], x21[i], line[i] = 675, 685, 695, 4
                            x12[i], y2[i], x22[i] = x12[i] + 62*rand, y2[i] + 62*rand, x22[i] + 62*rand
                        
                        if a[i] == 20:
                            stop[i] = True
                        elif a[i] == 10:
                            stop[i] = True
                            Money[i] = Money[i] - 2000
                        elif a[i] == 30:
                            a[i] = 10
                            stop[i] = True
                            Money[i] = Money[i] - 2000
                            x11[i], x12[i], y1[i], y2[i], x21[i], x22[i] = 25, 695, 35, 660, 45, 695
                        elif a[i] >= 40:
                            Money[i] = Money[i] + 1500
                        elif a[i] == 33 or a[i] == 17 or a[i] == 2:
                            Money[i] = Money[i] + 3000
                        elif a[i] == 12 or a[i] == 28:
                            Money[i] = Money[i] - 1500
                        
                        if a[i] == 1 or a[i] == 3:
                            if a[i] in active[x] or a[i] in active[y] or a[i] in active[z]:
                                if a[i] in active[x]:
                                    if 1 in active[x] and 3 in active[x]:
                                        Money[i] = Money[i] - 200
                                        Money[x] = Money[x] + 200
                                    else:
                                        Money[i] = Money[i] - 100
                                        Money[x] = Money[x] + 100
                                if a[i] in active[y]:
                                    if 1 in active[y] and 3 in active[y]:
                                        Money[i] = Money[i] - 200
                                        Money[y] = Money[y] + 200
                                    else:
                                        Money[i] = Money[i] - 100
                                        Money[y] = Money[y] + 100
                                if a[i] in active[z]:
                                    if 1 in active[z] and 3 in active[z]:
                                        Money[i] = Money[i] - 200
                                        Money[z] = Money[z] + 200
                                    else:
                                        Money[i] = Money[i] - 100
                                        Money[z] = Money[z] + 100
                            else:
                                pygame.draw.rect(sc, BLACK, (840, 145, 70, 30))
                                pygame.draw.rect(sc, BLACK, (920, 145, 115, 30))
                                font = pygame.font.SysFont('stxingkai', 25)
                                text1 = font.render("Цена 750, Купить    Отказаться", True, color[i])
                                text_rect = text1.get_rect()
                                text_x = 760
                                text_y = 150
                                sc.blit(text1, [text_x, text_y])
                                if yes == 1:
                                    yes = 0
                                    if a[i] == 1:
                                        active[i].append(1)
                                        Money[i] = Money[i] - 750
                                    elif a[i] == 3:
                                        active[i].append(3)
                                        Money[i] = Money[i] - 750 
                            
                        elif a[i] == 4 or a[i] == 38:
                            if a[i] == 4:
                                tax = len(active[i])*300 
                            else:
                                tax = len(active[i])*500
                            Money[i] = Money[i] - tax     

                        elif a[i] == 6 or a[i] == 8 or a[i] == 9:
                            if a[i] in active[x] or a[i] in active[y] or a[i] in active[z]:
                                if a[i] in active[x]:
                                    if 6 in active[x] and 8 in active[x] and 9 in active[x]:
                                        Money[i] = Money[i] - 500
                                        Money[x] = Money[x] + 500
                                    elif 6 in active[x] or 8 in active[x] or 9 in active[x]:
                                        Money[i] = Money[i] - 150
                                        Money[x] = Money[x] + 150
                                    else:
                                        Money[i] = Money[i] - 300
                                        Money[x] = Money[x] + 300
                                if a[i] in active[y]:
                                    if 6 in active[y] and 8 in active[y] and 9 in active[y]:
                                        Money[i] = Money[i] - 500
                                        Money[y] = Money[y] + 500
                                    elif 6 in active[y] or 8 in active[y] or 9 in active[y]:
                                        Money[i] = Money[i] - 150
                                        Money[y] = Money[y] + 150
                                    else:
                                        Money[i] = Money[i] - 300
                                        Money[y] = Money[y] + 300
                                if a[i] in active[z]:
                                    if 6 in active[z] and 8 in active[z] and 9 in active[z]:
                                        Money[i] = Money[i] - 500
                                        Money[z] = Money[z] + 500
                                    elif 6 in active[z] or 8 in active[z] or 9 in active[z]:
                                        Money[i] = Money[i] - 150
                                        Money[z] = Money[z] + 150
                                    else:
                                        Money[i] = Money[i] - 300
                                        Money[z] = Money[z] + 300
                            else:
                                pygame.draw.rect(sc, BLACK, (850, 145, 70, 30))
                                pygame.draw.rect(sc, BLACK, (930, 145, 115, 30))
                                font = pygame.font.SysFont('stxingkai', 25)
                                text1 = font.render("Цена 1000, Купить    Отказаться", True, color[i])
                                text_rect = text1.get_rect()
                                text_x = 760
                                text_y = 150
                                sc.blit(text1, [text_x, text_y])
                                if yes == 1:
                                    yes = 0
                                    if a[i] == 6:
                                        active[i].append(6)
                                        Money[i] = Money[i] - 1000
                                    elif a[i] == 8:
                                        active[i].append(8)
                                        Money[i] = Money[i] - 1000 
                                    elif a[i] == 9:
                                        active[i].append(9)
                                        Money[i] = Money[i] - 1000 
                            
                        elif a[i] == 11 or a[i] == 13 or a[i] == 14:
                            if a[i] in active[x] or a[i] in active[y] or a[i] in active[z]:
                                if a[i] in active[x]:
                                    if 11 in active[x] and 13 in active[x] and 14 in active[x]:
                                        Money[i] = Money[i] - 800
                                        Money[x] = Money[x] + 800
                                    elif 11 in active[x] or 13 in active[x] or 14 in active[x]:
                                        Money[i] = Money[i] - 250
                                        Money[x] = Money[x] + 250
                                    else:
                                        Money[i] = Money[i] - 500
                                        Money[x] = Money[x] + 500
                                if a[i] in active[y]:
                                    if 11 in active[y] and 13 in active[y] and 14 in active[y]:
                                        Money[i] = Money[i] - 800
                                        Money[y] = Money[y] + 800
                                    elif 11 in active[y] or 13 in active[y] or 14 in active[y]:
                                        Money[i] = Money[i] - 250                                            
                                        Money[y] = Money[y] + 250
                                    else:
                                        Money[i] = Money[i] - 500
                                        Money[y] = Money[y] + 500
                                if a[i] in active[z]:
                                    if 11 in active[z] and 13 in active[z] and 14 in active[z]:
                                        Money[i] = Money[i] - 800
                                        Money[z] = Money[z] + 800
                                    elif 11 in active[z] or 13 in active[z] or 14 in active[z]:
                                        Money[i] = Money[i] - 250
                                        Money[z] = Money[z] + 250
                                    else:
                                        Money[i] = Money[i] - 500
                                        Money[z] = Money[z] + 500
                            else:
                                pygame.draw.rect(sc, BLACK, (850, 145, 70, 30))
                                pygame.draw.rect(sc, BLACK, (935, 145, 115, 30))
                                font = pygame.font.SysFont('stxingkai', 25)
                                text1 = font.render("Цена 1250, Купить    Отказаться", True, color[i])
                                text_rect = text1.get_rect()
                                text_x = 760
                                text_y = 150
                                sc.blit(text1, [text_x, text_y])
                                if yes == 1:
                                    yes = 0
                                    if a[i] == 11:
                                        active[i].append(11)
                                        Money[i] = Money[i] - 1250
                                    elif a[i] == 13:
                                        active[i].append(13)
                                        Money[i] = Money[i] - 1250 
                                    elif a[i] == 14:
                                        active[i].append(14)
                                        Money[i] = Money[i] - 1250 

                        elif a[i] == 16 or a[i] == 18 or a[i] == 19:
                            if a[i] in active[x] or a[i] in active[y] or a[i] in active[z]:
                                if a[i] in active[x]:
                                    if 16 in active[x] and 18 in active[x] and 19 in active[x]:
                                        Money[i] = Money[i] - 1000
                                        Money[x] = Money[x] + 1000
                                    elif 16 in active[x] or 18 in active[x] or 19 in active[x]:
                                        Money[i] = Money[i] - 350
                                        Money[x] = Money[x] + 350
                                    else:
                                        Money[i] = Money[i] - 650
                                        Money[x] = Money[x] + 650
                                if a[i] in active[y]:
                                    if 16 in active[y] and 18 in active[y] and 19 in active[y]:
                                        Money[i] = Money[i] - 1000
                                        Money[y] = Money[y] + 1000
                                    elif 16 in active[y] or 18 in active[y] or 19 in active[y]:
                                        Money[i] = Money[i] - 350
                                        Money[y] = Money[y] + 350
                                    else:
                                        Money[i] = Money[i] - 650
                                        Money[y] = Money[y] + 650
                                if a[i] in active[z]:
                                    if 16 in active[z] and 18 in active[z] and 19 in active[z]:
                                        Money[i] = Money[i] - 1000
                                        Money[z] = Money[z] + 1000
                                    elif 16 in active[z] or 18 in active[z] or 19 in active[z]:
                                        Money[i] = Money[i] - 350
                                        Money[z] = Money[z] + 350
                                    else:
                                        Money[i] = Money[i] - 650
                                        Money[z] = Money[z] + 650
                            else:
                                pygame.draw.rect(sc, BLACK, (850, 145, 70, 30))
                                pygame.draw.rect(sc, BLACK, (935, 145, 115, 30))
                                font = pygame.font.SysFont('stxingkai', 25)
                                text1 = font.render("Цена 2000, Купить    Отказаться", True, color[i])
                                text_rect = text1.get_rect()
                                text_x = 760
                                text_y = 150
                                sc.blit(text1, [text_x, text_y])
                                if yes == 1:
                                    yes = 0
                                    if a[i] == 16:
                                        active[i].append(16)
                                        Money[i] = Money[i] - 2000
                                    elif a[i] == 18:
                                        active[i].append(18)
                                        Money[i] = Money[i] - 2000 
                                    elif a[i] == 19:
                                        active[i].append(9)
                                        Money[i] = Money[i] - 2000

                        elif a[i] == 21 or a[i] == 23 or a[i] == 24:
                            if a[i] in active[x] or a[i] in active[y] or a[i] in active[z]:
                                if a[i] in active[x]:
                                    if 21 in active[x] and 23 in active[x] and 24 in active[x]:
                                        Money[i] = Money[i] - 1500
                                        Money[x] = Money[x] + 1500
                                    elif 21 in active[x] or 23 in active[x] or 24 in active[x]:
                                        Money[i] = Money[i] - 550
                                        Money[x] = Money[x] + 550
                                    else:
                                        Money[i] = Money[i] - 900
                                        Money[x] = Money[x] + 900
                                if a[i] in active[y]:
                                    if 21 in active[y] and 23 in active[y] and 24 in active[y]:
                                        Money[i] = Money[i] - 1500
                                        Money[y] = Money[y] + 1500
                                    elif 21 in active[y] or 23 in active[y] or 24 in active[y]:
                                        Money[i] = Money[i] - 550
                                        Money[y] = Money[y] + 550
                                    else:
                                        Money[i] = Money[i] - 900
                                        Money[y] = Money[y] + 900
                                if a[i] in active[z]:
                                    if 21 in active[z] and 23 in active[z] and 24 in active[z]:
                                        Money[i] = Money[i] - 1500
                                        Money[z] = Money[z] + 1500
                                    elif 21 in active[z] or 23 in active[z] or 24 in active[z]:
                                        Money[i] = Money[i] - 550
                                        Money[z] = Money[z] + 550
                                    else:
                                        Money[i] = Money[i] - 900
                                        Money[z] = Money[z] + 900
                            else:
                                pygame.draw.rect(sc, BLACK, (850, 145, 70, 30))
                                pygame.draw.rect(sc, BLACK, (935, 145, 115, 30))
                                font = pygame.font.SysFont('stxingkai', 25)
                                text1 = font.render("Цена 3000, Купить    Отказаться", True, color[i])
                                text_rect = text1.get_rect()
                                text_x = 760                                    
                                text_y = 150
                                sc.blit(text1, [text_x, text_y])
                                if yes == 1:
                                    yes = 0
                                    if a[i] == 21:
                                        active[i].append(21)
                                        Money[i] = Money[i] - 3000
                                    elif a[i] == 23:
                                        active[i].append(23)
                                        Money[i] = Money[i] - 3000 
                                    elif a[i] == 24:
                                        active[i].append(24)
                                        Money[i] = Money[i] - 3000  
                            
                        elif a[i] == 26 or a[i] == 27 or a[i] == 29:
                            if a[i] in active[x] or a[i] in active[y] or a[i] in active[z]:
                                if a[i] in active[x]:
                                    if 26 in active[x] and 27 in active[x] and 29 in active[x]:
                                        Money[i] = Money[i] - 2000
                                        Money[x] = Money[x] + 2000
                                    elif 26 in active[x] or 27 in active[x] or 29 in active[x]:
                                        Money[i] = Money[i] - 750
                                        Money[x] = Money[x] + 750
                                    else:
                                        Money[i] = Money[i] - 1200
                                        Money[x] = Money[x] + 1200
                                if a[i] in active[y]:
                                    if 26 in active[y] and 27 in active[y] and 29 in active[y]:
                                        Money[i] = Money[i] - 2000
                                        Money[y] = Money[y] + 2000
                                    elif 21 in active[y] or 23 in active[y] or 24 in active[y]:
                                        Money[i] = Money[i] - 750
                                        Money[y] = Money[y] + 750
                                    else:
                                        Money[i] = Money[i] - 1200
                                        Money[y] = Money[y] + 1200
                                if a[i] in active[z]:
                                    if 26 in active[z] and 27 in active[z] and 29 in active[z]:
                                        Money[i] = Money[i] - 2000
                                        Money[z] = Money[z] + 2000
                                    elif 26 in active[z] or 27 in active[z] or 29 in active[z]:
                                        Money[i] = Money[i] - 750
                                        Money[z] = Money[z] + 750
                                    else:
                                        Money[i] = Money[i] - 1200
                                        Money[z] = Money[z] + 1200
                            else:
                                pygame.draw.rect(sc, BLACK, (850, 145, 70, 30))
                                pygame.draw.rect(sc, BLACK, (935, 145, 115, 30))
                                font = pygame.font.SysFont('stxingkai', 25)
                                text1 = font.render("Цена 4000, Купить    Отказаться", True, color[i])
                                text_rect = text1.get_rect()
                                text_x = 760
                                text_y = 150
                                sc.blit(text1, [text_x, text_y])
                                if yes == 1:
                                    yes = 0
                                    if a[i] == 26:
                                        active[i].append(26)
                                        Money[i] = Money[i] - 4000
                                    elif a[i] == 27:
                                        active[i].append(27)
                                        Money[i] = Money[i] - 4000 
                                    elif a[i] == 29:
                                        active[i].append(29)
                                        Money[i] = Money[i] - 4000

                        elif a[i] == 31 or a[i] == 32 or a[i] == 34:
                            if a[i] in active[x] or a[i] in active[y] or a[i] in active[z]:
                                if a[i] in active[x]:
                                    if 31 in active[x] and 32 in active[x] and 34 in active[x]:
                                        Money[i] = Money[i] - 2500
                                        Money[x] = Money[x] + 2500
                                    elif 31 in active[x] or 32 in active[x] or 34 in active[x]:
                                        Money[i] = Money[i] - 1000
                                        Money[x] = Money[x] + 1000
                                    else:
                                        Money[i] = Money[i] - 1900
                                        Money[x] = Money[x] + 1900
                                if a[i] in active[y]:
                                    if 31 in active[y] and 32 in active[y] and 34 in active[y]:
                                        Money[i] = Money[i] - 2500
                                        Money[y] = Money[y] + 2500
                                    elif 31 in active[y] or 32 in active[y] or 34 in active[y]:
                                        Money[i] = Money[i] - 1000
                                        Money[y] = Money[y] + 1000
                                    else:
                                        Money[i] = Money[i] - 1900
                                        Money[y] = Money[y] + 1900
                                if a[i] in active[z]:
                                    if 31 in active[z] and 32 in active[z] and 34 in active[z]:
                                        Money[i] = Money[i] - 2500
                                        Money[z] = Money[z] + 2500
                                    elif 31 in active[z] or 32 in active[z] or 34 in active[z]:
                                        Money[i] = Money[i] - 1000
                                        Money[z] = Money[z] + 1000
                                    else:
                                        Money[i] = Money[i] - 1900
                                        Money[z] = Money[z] + 1900
                            else:
                                pygame.draw.rect(sc, BLACK, (850, 145, 70, 30))
                                pygame.draw.rect(sc, BLACK, (935, 145, 115, 30))
                                font = pygame.font.SysFont('stxingkai', 25)
                                text1 = font.render("Цена 5000, Купить    Отказаться", True, color[i])
                                text_rect = text1.get_rect()
                                text_x = 760
                                text_y = 150
                                sc.blit(text1, [text_x, text_y])
                                if yes == 1:
                                    yes = 0
                                    if a[i] == 31:
                                        active[i].append(31)
                                        Money[i] = Money[i] - 5000
                                    elif a[i] == 32:
                                        active[i].append(32)
                                        Money[i] = Money[i] - 5000 
                                    elif a[i] == 34:
                                        active[i].append(34)
                                        Money[i] = Money[i] - 5000

                        elif a[i] == 37 or a[i] == 39:
                            if a[i] in active[x] or a[i] in active[y] or a[i] in active[z]:
                                if a[i] in active[x]:
                                    if 37 in active[x] and 39 in active[x]:
                                        Money[i] = Money[i] - 2500
                                        Money[x] = Money[x] + 2500
                                    else:
                                        Money[i] = Money[i] - 1500
                                        Money[x] = Money[x] + 1500
                                if a[i] in active[y]:
                                    if 37 in active[y] and 39 in active[y]:
                                        Money[i] = Money[i] - 2500
                                        Money[y] = Money[y] + 2500
                                    else:
                                        Money[i] = Money[i] - 1500
                                        Money[y] = Money[y] + 1500
                                if a[i] in active[z]:
                                    if 37 in active[z] and 39 in active[z]:
                                        Money[i] = Money[i] - 2500
                                        Money[z] = Money[z] + 2500
                                    else:
                                        Money[i] = Money[i] - 1500
                                        Money[z] = Money[z] + 1500
                            else:
                                pygame.draw.rect(sc, BLACK, (850, 145, 70, 30))
                                pygame.draw.rect(sc, BLACK, (935, 145, 115, 30))
                                font = pygame.font.SysFont('stxingkai', 25)
                                text1 = font.render("Цена 6000, Купить    Отказаться", True, color[i])
                                text_rect = text1.get_rect()
                                text_x = 760
                                text_y = 150
                                sc.blit(text1, [text_x, text_y])
                                if yes == 1:
                                    yes = 0
                                    if a[i] == 37:
                                        active[i].append(37)
                                        Money[i] = Money[i] - 6000
                                    elif a[i] == 39:
                                        active[i].append(39)
                                        Money[i] = Money[i] - 6000 

                        pygame.display.update()
                                    


                        font = pygame.font.SysFont('stxingkai', 25)
                        text1 = font.render("Ходит " + str(ruscolor[i]) + " игрок, поле " + str(a[i]), True, color[i])
                        text2 = font.render("Баланс игрока " + str(Money[i]), True, color[i])
                        text_rect = text1.get_rect()
                        text_x = 760
                        text_y = 50
                        text_y2 = 80
                        sc.blit(text1, [text_x, text_y])
                        sc.blit(text2, [text_x, text_y2])
                        pygame.display.update()
                        




                        
                    pygame.time.wait(1000)

                    pygame.draw.rect(sc, WHITE, (345, 250, 30, 30))
                    sc.blit(image, [0,0])
                    pygame.display.update()
                    query += 1

            pygame.display.update()


