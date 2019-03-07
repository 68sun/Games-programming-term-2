import pygame,sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("My first PyGame Program")
screen = pygame.display.set_mode((1280, 720))

ypos = 10

xpos = 20

clock = pygame.time.Clock()

while 1:
    
    pressed_key = pygame.key.get_pressed()

    clock.tick(200)
    

    #Drawing
    screen.fill((255,7,201))

    
    

    for i in range(5):
        
        pygame.draw.circle(screen, (0,i*8,255), (xpos + i * 50 , ypos), 25, i)

    if pressed_key[K_RIGHT]:
        xpos += 1

    elif pressed_key[K_LEFT]:
        xpos -= 1

    if pressed_key[K_DOWN]:
        ypos += 1

    elif pressed_key[K_UP]:
        ypos -= 1

    if ypos == 720:
        ypos = 0
    elif ypos == 0:
        ypos = 720

    if xpos == 1280:
        xpos = 0
    elif xpos == 0:
        xpos = 1280
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit


    pygame.display.update()


    
