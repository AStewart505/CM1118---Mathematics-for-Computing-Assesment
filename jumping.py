import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BROWN = (150, 75, 0)

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Jumping in PyGame")

X_POSITION, Y_POSITION = 50, 670

jumping = False

Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
PLAYER_VEL = 5

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("jummping/mario_standing.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("jummping/mario_jumping.png"), (48, 64))
BACKGROUND = pygame.transform.scale(pygame.image.load("Junglebackground.jpg"),(1400,800))\

rectangle1 = pygame.Rect(0,725,1400,75)
rectangle2 = pygame.Rect(0,700,1400,25)

mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True

    SCREEN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(SCREEN, BROWN, rectangle1)
    pygame.draw.rect(SCREEN, GREEN, rectangle2)
    
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
        

    pygame.display.update()
    CLOCK.tick(60)
