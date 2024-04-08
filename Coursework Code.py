import pygame 

image_filename ='Junglebackground.jpg'

from pygame.locals import *
from sys import exit

pygame.init() 


#Colour values set to given variables
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BROWN = (150, 75, 0)

#Sets the Default size of the screen
displayX = 1400
displayY = 800

BackgroundDefault = (displayX,displayY)

background = pygame.image.load(image_filename)

display_surface = pygame.display.set_mode((displayX, displayY)) 

#creates attributes for the floor
rectangle1 = pygame.Rect(0,725,1400,75)
rectangle2 = pygame.Rect(0,700,1400,25)

pygame.display.set_caption('Treasure Hunt')

background = pygame.transform.scale(background, BackgroundDefault)

display_surface.blit(background, (0,0))

pygame.display.flip()

#draws the floor
pygame.draw.rect(display_surface, BROWN, rectangle1)
pygame.draw.rect(display_surface, GREEN, rectangle2)

running = True

while running: 
	
    for event in pygame.event.get(): 
     
        
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()
            
        pygame.display.update()
        
