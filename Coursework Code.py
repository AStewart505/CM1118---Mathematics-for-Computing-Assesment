import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BROWN = (150, 75, 0)
GOLD = (255,215,0)
GREY = (105,105,105)

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Jumping in PyGame")

font = pygame.font.Font('freesansbold.ttf', 32)
level = 1
text = font.render('Level: ' + str(level), True, WHITE)
textRect = text.get_rect()
textRect.center = (100,40)

X_POSITION, Y_POSITION = 50, 670

jumping = False

Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
#Variables for Dart Projectile
dartAx=0
dartAy=0
dartBx=0
dartBy=0
dartCx=0
dartCy=0

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("mario_standing.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("mario_jumping.png"), (48, 64))
BACKGROUND = pygame.transform.scale(pygame.image.load("Junglebackground.jpg"),(1400,800))\

rectangle1 = pygame.Rect(0,725,1400,75)
rectangle2 = pygame.Rect(0,700,1400,25)
rectangle3 = pygame.Rect(0,0,0,0)
rectangle4 = pygame.Rect(0,0,0,0)
coinX, coinY = 1350, 670


mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_UP]:
        jumping = True

    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(text, (5, 10))
    pygame.draw.rect(SCREEN, BROWN, rectangle1)
    pygame.draw.rect(SCREEN, GREEN, rectangle2)
    pygame.draw.rect(SCREEN, BROWN, rectangle3)
    pygame.draw.rect(SCREEN, GREEN, rectangle4)
    COIN = pygame.draw.circle(SCREEN,GOLD,(coinX,coinY),20,0)
    pygame.draw.polygon(SCREEN,GREY,[(dartAx,dartAy),(dartBx,dartBy),(dartCx,dartCy)])
    
    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        mario_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, mario_rect)
    else:
        mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, mario_rect)
        
    
    if keys_pressed[pygame.K_LEFT]:
        X_POSITION = X_POSITION - 5

    if keys_pressed[pygame.K_RIGHT]:
        X_POSITION = X_POSITION + 5

    if X_POSITION == 1350 and level == 1:
        level += 1
        text = font.render('Level: ' + str(level), True, WHITE)
        textRect = text.get_rect()
        textRect.center = (100, 40)
        rectangle1 = pygame.Rect(0,725,650,75)
        rectangle2 = pygame.Rect(0,700,650,25)
        X_POSITION, Y_POSITION = 50, 670
        rectangle3 = pygame.Rect(750,725,650,75)
        rectangle4 = pygame.Rect(750,700,650,25)

    if X_POSITION > 650 and X_POSITION < 750 and level > 1 and Y_POSITION > 651:
        Y_POSITION += 5

    if Y_POSITION == 800:
        X_POSITION, Y_POSITION = 50, 670

    if X_POSITION == 1350 and level == 2:
        level += 1
        text = font.render('Level: ' + str(level), True, WHITE)
        textRect = text.get_rect()
        textRect.center = (100, 40)
        rectangle1 = pygame.Rect(0,725,650,75)
        rectangle2 = pygame.Rect(0,700,650,25)
        X_POSITION, Y_POSITION = 50, 670
        rectangle3 = pygame.Rect(750,725,650,75)
        rectangle4 = pygame.Rect(750,700,650,25)
        dartAx=1200
        dartAy=625
        dartBx=1200
        dartBy=675
        dartCx=1100
        dartCy=650

    if level == 3:
        #CODE FOR DART PROJECTILE MOTION
        pygame.time.delay(15)
        for counter in range(15):
            dartAx-=0.5
            dartBx-=0.5
            dartCx-=0.5    
            dartAy +=0.01
            dartBy +=0.01
            dartCy +=0.01 
    
    if level == 3 and dartCx == X_POSITION and dartCy == Y_POSITION:
        X_POSITION, Y_POSITION = 50, 670
        dartAx=1200
        dartAy=625
        dartBx=1200
        dartBy=675
        dartCx=1100
        dartCy=650

    if level == 3 and X_POSITION == 1350:
        rectangle1 = pygame.Rect(0,0,0,0)
        rectangle2 = pygame.Rect(0,0,0,0)
        rectangle3 = pygame.Rect(0,0,0,0)
        rectangle4 = pygame.Rect(0,0,0,0)
        dartAx=0
        dartAy=0
        dartBx=0
        dartBy=0
        dartCx=0
        dartCy=0
        X_POSITION, Y_POSITION = 5000, 5000
        coinX = 5000
        coinY = 5000
        textRect.center = (500,500)
        BACKGROUND = pygame.transform.scale(pygame.image.load("youWin.webp"),(1400,800))\



    pygame.display.update()
    CLOCK.tick(60)
