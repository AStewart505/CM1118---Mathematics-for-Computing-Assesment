import pygame 
from pygame.locals import *

pygame.init() 


#Colour values set to given variables
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)




window = pygame.display.set_mode((1400, 800)) 

pygame.display.set_caption('Drawing')

window.fill(BLUE)

pygame.draw.polygon(window, BLUE, 
					[(200, 0), (200,200), (400,0), 
					(400, 400),], 20) 
					

pygame.draw.line(window, BLUE, 
				(60, 300), (120, 300), 4) 

window.fill(WHITE)
pygame.display.flip()





running = True

while running: 
	
    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: 
            running = False