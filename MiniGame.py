import pygame
import sys
import random
pygame.init()

sc = pygame.display.set_mode((700,800))
pygame.display.set_caption("Блоки")
pygame.display.flip()

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255, 255, 0)
game_over = False
k = False
x = 350
y = 700




def game():
    image = pygame.image.load('F:\PyGame\png\space.jpg')
    raketa = pygame.image.load('F:\PyGame\png\Raketa1.png')
    cometa = pygame.image.load('F:\PyGame\png\cometa.png')
    guns = pygame.image.load('F:\PyGame\png\gun.png')
    boom = pygame.image.load('F:\PyGame\png\взрыв.png')
    protect = pygame.image.load('F:\PyGame\png\иконкаЩита.png')
    protect1 = pygame.image.load('F:\PyGame\png\щит.png')
    WHITE = (255, 255, 255)
    RED = (225, 0, 50)
    GREEN = (0, 225, 0)
    BLUE = (0, 0, 225)
    BLACK = (0,0,0)
    GREY = (128,128,128)
    YELLOW = (255, 255, 0)
    game_over = False
    count = 0
    a = 0
    gun = 1
    defs = False
    k = False
    d = False
    x = 300
    lol = True


    pygame.display.update()
    ### стартовые координаты метеоров и скорость
    y1, sp1 = random.randint(-375, -125), random.randint(2, 4)
    y2, sp2 = random.randint(-375, - 125), random.randint(2, 4)
    y3, sp3 = random.randint(-375, - 125), random.randint(2, 4)
    y4, sp4 = random.randint(-375, - 125), random.randint(2, 4)
    y5, sp5 = random.randint(-375, - 125), random.randint(2, 4)
    y6, sp6 = random.randint(-375, - 125), random.randint(2, 4)
    sc.blit(raketa, [x, 700])
    yyy = -125
    yyy1 = -125
    pause = False
    xGo = False
    xGo1 = False
    countA = 0
    countB = 0

    while True:
        if not game_over:
            ### очки и количество патронов в левой верхней части экрана
            font = pygame.font.SysFont('stxingkai', 25)
            text1 = font.render("Score: "+ str(count) + "    gun: "+str(gun), True, WHITE)
            text_rect = text1.get_rect()
            text_x = 25
            text_y = 25
            sc.blit(text1, [text_x, text_y])
            ### генерация патронов и щитов
            if k == False:
                rand = random.randint(0,1000)
                r = random.randint(0, 5)
                if rand == 500:
                    sc.blit(guns,[r*100+30, yyy])
                    k = True

            if d == False:
                rand1 = random.randint(0,1000)
                r1 = random.randint(0, 5)
                if rand1 == 700:
                    sc.blit(protect, [r1*100+5, yyy1])
                    d = True
            ### отрисовка патрона и щита
            if d:
                sc.blit(protect, [r1*100-5, yyy1])
            if yyy>900:
                d = False
                yyy1 = -125
            if k==True:
                sc.blit(guns,[r*100+30, yyy])
            if yyy>900:
                k = False
                yyy = -125


            ### кометы и ракета
            sc.blit(raketa, [x, 700])
            if defs:
                sc.blit(protect1, [x-20, 680])

            sc.blit(cometa, [15, y1])
            sc.blit(cometa, [115, y2])
            sc.blit(cometa, [225, y3])
            sc.blit(cometa, [335, y4])
            sc.blit(cometa, [445, y5])
            sc.blit(cometa, [555, y6])
            pygame.draw.line(sc, RED, (105, 0), (105, 800), 5)
            pygame.draw.line(sc, RED, (115, 0), (115, 800), 5)
            pygame.draw.line(sc, RED, (200, 0), (200, 800), 5)
            pygame.draw.line(sc, RED, (225, 0), (225, 800), 5)
            pygame.draw.line(sc, RED, (315, 0), (315, 800), 5)
            pygame.draw.line(sc, RED, (335, 0), (335, 800), 5)
            pygame.draw.line(sc, RED, (430, 0), (430, 800), 5)
            pygame.draw.line(sc, RED, (445, 0), (445, 800), 5)
            pygame.draw.line(sc, RED, (540, 0), (540, 800), 5)
            pygame.draw.line(sc, RED, (555, 0), (555, 800), 5)
            pygame.draw.line(sc, RED, (650, 0), (650, 800), 5)
            pygame.display.update()

            ### проверка на крайний ряд, переброс с 1 на 6 дорожку и наоборот
            if x < 0:
                x = 600
            if x > 700:
                x = 0

            ### столкновения и взаимодействия с ракетой
            if x>=0 and x<105:
                if yyy >= 700 and yyy-50 <=790:
                    k = False
                if y1+125 >= 700 and y1 <= 790:
                    if defs == True:
                        defs = False
                        y1 = random.randint(-375, - 125)
                        sp1 = random.randint(2, 4)
                    else:
                        game_over = True
                elif a >=15 and a<=105:
                    for i in range(5):
                        sc.blit(boom, [5, y1])
                        pygame.display.update()
                    y1 = random.randint(-375, - 125)
                    a = 0
            elif x>=115 and x<200:
                if yyy >= 700 and yyy-50 <=790:
                    k = False
                if y2+125 >= 700 and y2 <= 790:
                    if defs:
                        defs = False
                        y2 = random.randint(-375, - 125)
                        sp2 = random.randint(2, 4)
                    else:
                        game_over = True
                elif a >=115 and a<=205:
                    for i in range(5):
                        sc.blit(boom, [105, y2])
                        pygame.display.update()
                    y2 = random.randint(-375, - 125)
                    a = 0
            elif x>=225 and x<315:
                if yyy >= 700 and yyy-50 <=790:
                    k = False
                if y3+125 >= 700 and y3 <= 790:
                    if defs:
                        defs = False
                        y3 = random.randint(-375, - 125)
                        sp3 = random.randint(2, 4)
                    else:
                        game_over = True
                elif a >225 and a<315:
                    for i in range(5):
                        sc.blit(boom, [205, y3])
                        pygame.display.update()
                    y3 = random.randint(-375, - 125)
                    a = 0
            elif x>=335 and x<430:
                if yyy >= 700 and yyy-50 <=790:
                    k = False
                if y4+125 >= 700 and y4 <= 790:
                    if defs:
                        defs = False
                        y4 = random.randint(-375, - 125)
                        sp4 = random.randint(2, 4)
                    else:
                        game_over = True
                elif a >335 and a<430:
                    for i in range(5):
                        sc.blit(boom, [305, y4])
                        pygame.display.update()
                    y4 = random.randint(-375, - 125)
                    a = 0
            elif x>=445 and x<540:
                if yyy >= 700 and yyy-50 <=790:
                    k = False
                if y5+125 >= 700 and y5 <= 790:
                    if defs:
                        defs = False
                        y5 = random.randint(-375, - 125)
                        sp5 = random.randint(2, 4)
                    else:
                        game_over = True
                elif a >445 and a<540:
                    for i in range(5):
                        sc.blit(boom, [405, y5])
                        pygame.display.update()
                    y5 = random.randint(-375, - 125)
                    a = 0
            elif x>=555 and x<650:
                if yyy >= 700 and yyy-50 <=790:
                    k = False
                if y6+125 >= 700 and y6 <= 790:
                    if defs:
                        defs = False
                        y6 = random.randint(-375, - 125)
                        sp6 = random.randint(2, 4)
                    else:
                        game_over = True
                elif a >555 and a<650:
                    for i in range(5):
                        sc.blit(boom, [505, y6])
                        pygame.display.update()
                    y6 = random.randint(-375, - 125)
                    a = 0
            ### подбор патрона
            if rand == 500 and x >= r*100 and x<r*100+100 and yyy >= 650 and yyy-50 <= 800:
                gun += 3
                rand = 0
                k = False
            if rand1 == 700 and x >= r*100 and x<r*100+100 and yyy1 >= 650 and yyy1-50<=800:
                defs = True
                d = False
                rand1 = 0

                
            ### при пролёте метеорита через экран новая отрисовка
            if y1 > 800:
                y1 = random.randint(-375, - 125)
                sp1 = random.randint(2, 4)
                count += 1
            if y2 > 800:
                y2 = random.randint(-375, - 125)
                sp2 = random.randint(2, 4)
                count += 1
            if y3 > 800:
                y3 = random.randint(-375, - 125)
                sp3 = random.randint(2, 4)
                count += 1
            if y4 > 800:
                y4 = random.randint(-375, - 125)
                sp4 = random.randint(2, 4)
                count += 1
            if y5 > 800:
                y5 = random.randint(-375, - 125)
                sp5 = random.randint(2, 4)
                count += 1
            if y6 > 800:
                y6 = random.randint(-375, - 125)
                sp6 = random.randint(2, 4)
                count += 1
            pygame.display.update()
            ### проверка на клавиши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                    break
                elif event.type == pygame.KEYDOWN and not game_over:
                    if event.key == pygame.K_LEFT:
                        xGo = True
                        pause = False
                    elif event.key == pygame.K_RIGHT:
                        xGo1 = True
                        pause = False
                    elif event.key == pygame.K_SPACE:
                        if gun > 0:
                            for i in range(7):
                                pygame.draw.circle(sc, YELLOW, (x+45, 690), 30)
                                pygame.draw.line(sc, RED, (x+50, 640), (x+50, 0), 3)
                                pygame.display.update()
                                a = 0
                            a = x+50
                            gun -= 1
                    elif event.key == pygame.K_p:
                        pause = True
                elif game_over:
                    if event.type == pygame.KEYDOWN and game_over:
                        game_over = False

            ### скорость метеоритов
            if not pause:
                yyy += 2
                yyy1 += 2
                y1 += sp1
                y2 += sp2
                y3 += sp3
                y4 += sp4
                y5 += sp5
                y6 += sp6
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    x -= 5
                if keys[pygame.K_RIGHT]:
                    x += 5
                pygame.display.update()
                sc.blit(image, [0, 0])
  
        ### окончание игры
        elif game_over:
            sc.fill(BLACK)
            font = pygame.font.SysFont('stxingkai', 45)
            text1 = font.render("Вы проиграли, ваши очки: "+str(count), True, RED)
            text_rect = text1.get_rect()
            text_x = 140
            text_y = 375
            sc.blit(text1, [text_x, text_y])
            pygame.display.update()
            game_over = False
            menu()




### меню игры
def menu():
    ### кнопки
    pygame.draw.rect(sc, GREEN, (225, 200, 225, 45))
    font = pygame.font.SysFont('stxingkai', 35)
    text1 = font.render("Играть", True, RED)
    text_rect = text1.get_rect()
    text_x = 295
    text_y = 210
    sc.blit(text1, [text_x, text_y])

    pygame.draw.rect(sc, GREEN, (225, 500, 225, 45))
    font = pygame.font.SysFont('stxingkai', 35)
    text1 = font.render("Выйти", True, RED)
    text_rect = text1.get_rect()
    text_x = 295
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
                if x_mouse > 225 and x_mouse < 450:
                    if y_mouse > 200 and y_mouse < 245:
                        game()
                    elif y_mouse > 500 and y_mouse < 545:
                        pygame.quit()
                        sys.exit(0)
        
menu()

