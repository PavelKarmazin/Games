from re import T
import pygame
import sys
import random
from pymunk import Space
import pymunk.pygame_util
sc = pygame.display.set_mode((349, 472))
pymunk.pygame_util.positive_y_is_up = False
pygame.init()
pygame.display.set_caption("Потом придумаю")
pygame.display.flip()
###
fon1 = pygame.image.load(r'F:\PyGame\png\zombie\fon1.png')
zombie = pygame.image.load(r'F:\PyGame\png\zombie\zombie.png')
sklet = pygame.image.load(r'F:\PyGame\png\zombie\sklet.png')
prizrak = pygame.image.load(r'F:\PyGame\png\zombie\prizrak.png')
zombie2 = pygame.image.load(r'F:\PyGame\png\zombie\zombie2.png')
sklet2 = pygame.image.load(r'F:\PyGame\png\zombie\sklet2.png')
prizrak2 = pygame.image.load(r'F:\PyGame\png\zombie\prizrak2.png')
shinigami = pygame.image.load(r'F:\PyGame\png\zombie\shinigami.png')
shinigami2 = pygame.image.load(r'F:\PyGame\png\zombie\shinigami2.png')
fon2 = pygame.image.load(r'F:\PyGame\png\zombie\fon2.JPG')
dragon = pygame.image.load(r'F:\PyGame\png\zombie\dragon.png')
dragon2 = pygame.image.load(r'F:\PyGame\png\zombie\dragon2.png')
kosa = pygame.image.load(r'F:\PyGame\png\zombie\kosa.png')
kosa2 = pygame.image.load(r'F:\PyGame\png\zombie\kosa2.png')
kosaUdar = pygame.image.load(r'F:\PyGame\png\zombie\kosaUdar.png')
kosa2Udar = pygame.image.load(r'F:\PyGame\png\zombie\kosa2Udar.png')
zelua = pygame.image.load(r'F:\PyGame\png\zombie\zelya.jpg')
lose = pygame.image.load(r'F:\PyGame\png\zombie\lose.jpg')
dw_op = pymunk.pygame_util.DrawOptions(sc)
clock = pygame.time.Clock()
###
prov1 = False
prov2 = False
def game(): 
    sc = pygame.display.set_mode((1300,900))
    global prov1, prov2
    a = 20
    FPS = 70
    x = 0
    y = 10
    pos = True
    space = pymunk.Space()
    space.gravity = 0, 500
    timer = 30
    up = False
    zomX, prizX, sklX, dragX, sklX2 = 600, 900, 1200, 1100, 0
    zomGo1 = True
    prizGo1 = True
    sklGo1 = True
    dragGo1 = True
    udar = False
    sklGo2 = True
    xp = 200
    dmg1 = 80
    dmg2 = 300
    xpSkl1 = 250
    xpSkl2 = 250
    xpPriz1 = 220
    xpPriz2 = 220
    xpZom1 = 350
    xpDragon = 1000
    dmgSkl = 1
    dmgPriz = 1
    dmgZom = 2
    dmgDragon = 5
    yDragon = 0
    FinalBoss = False
    DragUp = False
    corXR, corYR = [], []
    corXL, corYL = [], []
    udar1 = False
    udar2 = False
    a1 = 130
    a2 = 130
    def chekDamag(damage, xVrag, yVrag, long, height):
        global prov1, prov2
        if x in range(xVrag, xVrag+long) or x+150 in range(xVrag, xVrag+long):
            prov1 = True
        if yVrag in range(p[1], p[1]+130) or yVrag+height in range(p[1], p[1]+130):
            prov2 = True
        if prov1 and prov2:
            return True
        prov1, prov2 = False, False

    def chekUdar(xKosa, yKosa, xVrag, yVrag, long, height):
        if xKosa in range(xVrag, xVrag+long) and yKosa in range(yVrag, yVrag+height):
            return True
    ###
    platformD = pymunk.Segment(space.static_body, (1, 900), (1300, 900), 1)
    platformD.filter = pymunk.ShapeFilter(categories=0b1000)
    platformD.elasticy = 0.4
    platformD.friction = 1.0
    space.add(platformD)
    ###
    platformD1 = pymunk.Segment(space.static_body, (200, 700), (1300, 700), 5)
    platformD1.filter = pymunk.ShapeFilter(categories=0b1000)
    platformD1.elasticy = 0.4
    platformD1.friction = 1.0
    space.add(platformD1)
    ###
    platformD2 = pymunk.Segment(space.static_body, (0, 500), (800, 500), 5)
    platformD2.filter = pymunk.ShapeFilter(categories=0b1000)
    platformD2.elasticy = 0.4
    platformD2.friction = 1.0
    space.add(platformD2)
    ###
    platformD3 = pymunk.Segment(space.static_body, (200, 300), (1100, 300), 5)
    platformD3.filter = pymunk.ShapeFilter(categories=0b1000)
    platformD3.elasticy = 0.4
    platformD3.friction = 1.0
    space.add(platformD3)
    ###
    body = pymunk.Body(5, float("inf"))
    body.position = x, y
    head = pymunk.Circle(body, 20, (90, 25))
    head2 = pymunk.Circle(body, 21, (88, 75))
    feet = pymunk.Circle(body, 15, (90, 120))
    mask = pymunk.ShapeFilter.ALL_MASKS() 
    sf = pymunk.ShapeFilter(mask=mask)
    head.filter = sf
    head2.filter = sf
    feet.collision_type = 1
    feet.ignore_draw = head.ignore_draw = head2.ignore_draw = True
    space.add(body, head2, head, feet)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
        prov1, prov2 = False, False
        body.position = x, y
        space.step(1/FPS)
        space.debug_draw(dw_op)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x+=4
            pos = True
        if keys[pygame.K_LEFT]:
            x-=4
            pos = False
        if keys[pygame.K_UP] and timer<0:
            timer = 60
            up = True
        if up:
            body.position = x, y-5
        if keys[pygame.K_SPACE] and a<=0:
            a = 20
            udar = True
        elif keys[pygame.K_SPACE] and a1<=0 and keys[pygame.K_DOWN] and pos:
            a1 = 130
            udar1 = True
            yKosa = y
            xKosa = x
        elif keys[pygame.K_SPACE] and a1<=0 and keys[pygame.K_DOWN] and not pos:
            a2 = 130
            udar2 = True
            yKosa = y
            xKosa = x
        position = body.position
        p = pymunk.pygame_util.to_pygame(position, sc)
        if pos:
            sc.blit(shinigami, p)
            if not udar:
                sc.blit(kosa, [x+60, y-20])
        if not pos:
            sc.blit(shinigami2, [p[0]+11, p[1]])
            if not udar:
                sc.blit(kosa2, [x+35, y-20])
        pygame.display.update()
        sc.blit(fon2, [0,0])
        clock.tick(FPS)
        y = p[1]
        timer -= 1
        if timer == 20:
            up = False
        ###
        if xpZom1>0:
            if zomX == 220:
                zomGo1 = False
            elif zomX == 1200:
                zomGo1 = True
            if zomGo1:
                zomX -= 2
                sc.blit(zombie2, [zomX, 190])
            else:
                zomX += 2
                sc.blit(zombie, [zomX, 190])
            if x>zomX and y<200:
                zomGo1 = False
            elif x<zomX and y<200:
                zomGo1 = True
        ###
        if prizX == 0:
            prizGo1 = False
        elif prizX == 999:
            prizGo1 = True
        if prizGo1:
            if xpPriz2>0:
                sc.blit(prizrak2, [prizX, 800])
            if xpPriz1>0:
                sc.blit(prizrak2, [prizX, 400])
            prizX -= 3
        else:
            if xpPriz2>0:
                sc.blit(prizrak, [prizX, 800])
            if xpPriz1>0:
                sc.blit(prizrak, [prizX, 400])
            prizX += 3
        if x>prizX and y>300 and y<500:
                prizGo1 = False
        elif x<prizX and ((y>300 and y<500) or y<800):
                prizGo1 = True
        ###
        if xpSkl1>0:
            if sklX == 400:
                sklGo1 = False
            elif sklX == 1200:
                sklGo1 = True
            if sklGo1:
                sc.blit(sklet2, [sklX, 580])
                sklX -= 2
            else:
                sc.blit(sklet, [sklX, 580])
                sklX += 2
            if x>sklX and y<580:
                sklGo1 = False
            elif x<sklX and y>580:
                sklGo1 = True
        ###

        if xpSkl2>0:
            if sklX2 == 1300:
                sklGo2 = False
            elif sklX2 == 0:
                sklGo2 = True
            if sklGo2:
                sc.blit(sklet, [sklX2, 780])
                sklX2 += 2
            else:
                sc.blit(sklet2, [sklX2, 780])
                sklX2 -= 2
        ###
        if udar:
            if pos:
                sc.blit(kosaUdar, [x+70, y+50])
            else:
                sc.blit(kosa2Udar, [x-70, y+50])
        if udar1:
            sc.blit(kosaUdar, [xKosa, yKosa+30])
            xKosa += 4
        elif udar2:
            sc.blit(kosa2Udar, [xKosa-30, yKosa+30])
            xKosa -= 4
        if a==0:
            udar = False
        if a1==0:
            udar1 = False
        if a2==0:
            udar2 = False


        ###
        pygame.draw.rect(sc, 'red', (x+40, y-50, 100, 20))
        pygame.draw.rect(sc, 'green', (x+40, y-50, xp//2, 20))
        ###
        if xpDragon>0 and FinalBoss:
            pygame.draw.rect(sc, 'red', (400, 10, 500, 30))
            pygame.draw.rect(sc, 'green', (400, 10, xpDragon//2, 30))
        if xpPriz1>0:
            pygame.draw.rect(sc, 'red', (prizX-10, 350, 100, 20))
            pygame.draw.rect(sc, 'green', (prizX-10, 350, xpPriz1//2, 20))
        if xpPriz2>0:
            pygame.draw.rect(sc, 'red', (prizX-10, 750, 100, 20))
            pygame.draw.rect(sc, 'green', (prizX-10, 750, xpPriz2//2, 20))
        if xpZom1>0:
            pygame.draw.rect(sc, 'red', (zomX-40, 170, 175, 20))
            pygame.draw.rect(sc, 'green', (zomX-40, 170, xpZom1//2, 20))
        if xpSkl1>0:
            pygame.draw.rect(sc, 'red', (sklX-15, 560, 125, 20))
            pygame.draw.rect(sc, 'green', (sklX-15, 560, xpSkl1//2, 20))
        if xpSkl2>0:
            pygame.draw.rect(sc, 'red', (sklX2-15, 760, 125, 20))
            pygame.draw.rect(sc, 'green', (sklX2-15, 760, xpSkl2//2, 20))
        if xpPriz2>0:
            if chekDamag(dmgPriz ,prizX, 800, 75, 80):
                xp -= dmgPriz
        if xpPriz1>0:
            if chekDamag(dmgPriz ,prizX, 400, 75, 80):
                xp -= dmgPriz
        if xpZom1>0:
            if chekDamag(dmgZom ,zomX, 190, 77, 110):
                xp -= dmgZom
        if xpSkl1>0:
            if chekDamag(dmgSkl ,sklX, 580, 75, 128):
                xp -= dmgSkl
        if pos:
            kosaX = x+160+60
        elif not pos:
            kosaX = x - 50
        if udar:
            if chekUdar(kosaX, y+50, prizX, 400, 75, 80) and a==20:
                xpPriz1 -= dmg1
            if chekUdar(kosaX, y+50, prizX, 800, 75, 80) and a==20:
                xpPriz2 -= dmg1
            if chekUdar(kosaX, y+50, zomX, 190, 77, 110) and a==20:
                xpZom1 -= dmg1
            if chekUdar(kosaX, y+50, sklX, 580, 75, 128) and a==20:
                xpSkl1 -= dmg1
            if chekUdar(kosaX, y+50, sklX2, 780, 75, 128) and a==20:
                xpSkl2 -= dmg1
        elif udar1:
            if chekUdar(xKosa+100, yKosa+50, prizX, 400, 75, 80):
                xpPriz1 -= 5
            if chekUdar(xKosa+100, yKosa+50, prizX, 800, 75, 80):
                xpPriz2 -= 5
            if chekUdar(xKosa+100, yKosa+50, zomX, 190, 77, 110):
                xpZom1 -= 5
            if chekUdar(xKosa+100, yKosa+50, sklX, 580, 75, 128):
                xpSkl1 -= 5
            if chekUdar(xKosa+100, yKosa+50, sklX2, 780, 75, 128):
                xpSkl2 -= 5
        elif udar2:
            if chekUdar(xKosa, yKosa+50, prizX, 400, 75, 80):
                xpPriz1 -= 5
            if chekUdar(xKosa, yKosa+50, prizX, 800, 75, 80):
                xpPriz2 -= 5
            if chekUdar(xKosa, yKosa+50, zomX, 190, 77, 110):
                xpZom1 -= 5
            if chekUdar(xKosa, yKosa+50, sklX, 580, 75, 128):
                xpSkl1 -= 5
            if chekUdar(xKosa, yKosa+50, sklX2, 780, 75, 128):
                xpSkl2 -= 5

        if xpPriz1 <= 0 and xpPriz2 <=0 and xpSkl1 <= 0 and xpSkl2 <= 0 and xpZom1 <= 0:
            if xp<200:
                xp += 1
            if chekDamag(dmgDragon, dragX, yDragon+100, 280, 150):
                xp -= dmgDragon
            if udar:
                if chekUdar(kosaX, y+50, dragX, yDragon, 280, 250) and a==20:
                    xpDragon -= dmg1
            elif udar1:
                if chekUdar(xKosa+100, yKosa+50, dragX, yDragon, 280, 250):
                    xpDragon -= 4
            elif udar2:
                if chekUdar(xKosa, yKosa+50, dragX, yDragon, 280, 250):
                    xpDragon -= 4

            FinalBoss = True
            if not DragUp:
                if dragX < 180 and yDragon<250:
                    yDragon+=3
                if dragX>800 and yDragon>=240 and yDragon < 440:
                    yDragon+=3
                if dragX<250 and yDragon >= 430 and yDragon < 620:
                    yDragon+=3
                if yDragon>=620 and dragX>800:
                    DragUp = True
            if DragUp:
                if dragX < 180 and yDragon<250:
                    yDragon-=3
                if dragX>800 and yDragon>=240 and yDragon < 440:
                    yDragon-=3
                if dragX<250 and yDragon >= 430:
                    yDragon-=3
                if yDragon<0:
                    DragUp = False
            if dragX == 0:
                dragGo1 = False
            elif dragX == 1000:
                dragGo1 = True
            if dragGo1:
                sc.blit(dragon2, [dragX, yDragon])
                dragX -= 4
            else:
                sc.blit(dragon, [dragX, yDragon])
                dragX += 4

            
        if xpDragon <= 0:
            for _ in range(700):
                sc.fill('black')
                font = pygame.font.SysFont('stxingkai', 60)
                text1 = font.render("You win!", True, 'blue')
                text_rect = text1.get_rect()
                text_x = 530
                text_y = 220
                sc.blit(text1, [text_x, text_y])
                font = pygame.font.SysFont('stxingkai', 60)
                text1 = font.render("Слава Украине!", True, 'yellow')
                text_rect = text1.get_rect()
                text_x = 450
                text_y = 420
                sc.blit(text1, [text_x, text_y])
                pygame.display.update()
            sc.fill('black')
            menu()
        if xp <= 0:
            for _ in range(700):
                sc = pygame.display.set_mode((514, 406))
                sc.blit(lose, [0, 0])
                pygame.display.update()
            menu()
        a-=1
        a1-=1
        a2-=1

def menu():
    sc = pygame.display.set_mode((349, 472))
    sc.blit(zelua, [0, 0])
#    pygame.draw.rect(sc, 'green', (500, 200, 225, 45))
    font = pygame.font.SysFont('stxingkai', 35)
    text1 = font.render("Играть", True, 'red')
    text_rect = text1.get_rect()
    text_x = 175
    text_y = 230
    sc.blit(text1, [text_x, text_y])

 #   pygame.draw.rect(sc, 'green', (500, 500, 225, 45))
    font = pygame.font.SysFont('stxingkai', 35)
    text1 = font.render("Выйти", True, 'red')
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
                if x_mouse > 175 and x_mouse < 245:
                    if y_mouse > 230 and y_mouse < 255:
                        game()

menu()        

