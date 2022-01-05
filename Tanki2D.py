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
x = 550
y = 800
tankUp = True
tankR = False
TankL = False
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
    sc.blit(block, [0,100])
    sc.blit(block, [100,100])
    sc.blit(block, [200,100])
    sc.blit(block, [300,100])
    sc.blit(block, [400,100])

    sc.blit(block, [1100,100])
    sc.blit(block, [1000,100])
    sc.blit(block, [900,100])
    sc.blit(block, [800,100])
    sc.blit(block, [700,100])

    sc.blit(block, [400,100])
    sc.blit(block, [400,200-23*2])
    sc.blit(block, [400,300-23*3])
    sc.blit(block, [400,400-23*4])
    sc.blit(block, [400,500-23*5])
    sc.blit(block, [400,600-23*6])
    sc.blit(block, [400,700-23*7])

    sc.blit(block, [700,100])
    sc.blit(block, [700,200-23*2])
    sc.blit(block, [700,300-23*3])
    sc.blit(block, [700,400-23*4])
    sc.blit(block, [700,500-23*5])
    sc.blit(block, [700,600-23*6])
    sc.blit(block, [700,700-23*7])

    sc.blit(block, [800,400-23*4])
    sc.blit(block, [900,400-23*4])
    sc.blit(block, [800,700-23*7])
    sc.blit(block, [900,700-23*7])

    sc.blit(block, [300,400-23*4])
    sc.blit(block, [200,400-23*4])
    sc.blit(block, [300,700-23*7])
    sc.blit(block, [200,700-23*7])

    sc.blit(block, [300,900-20*9])
    sc.blit(block, [400,900-20*9])
    sc.blit(block, [500,900-20*9])
    sc.blit(block, [600,900-20*9])
    sc.blit(block, [700,900-20*9])
    sc.blit(block, [800,900-20*9])

    if tankUp:
        sc.blit(tank, [x, y])
    elif tankR:
        sc.blit(tank1, [x, y])
    elif tankD:
        sc.blit(tank2, [x, y])
    elif TankL:
        sc.blit(tank3, [x, y])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
        tankUp = False
        tankR = False
        TankL = True
        tankD = False
    if keys[pygame.K_RIGHT]:
        x += 5
        tankUp = False
        tankR = True
        TankL = False
        tankD = False
    if keys[pygame.K_UP]:
        y -= 5
        tankUp = True
        tankR = False
        TankL = False
        tankD = False
    if keys[pygame.K_DOWN]:
        y += 5
        tankUp = False
        tankR = False
        TankL = False
        tankD = True

    pygame.display.update()
    sc.fill(BLACK)



        