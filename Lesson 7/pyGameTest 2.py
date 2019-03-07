import pygame,sys, random, time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("My first PyGame Program")
screen = pygame.display.set_mode((1280, 720))

pygame.font.init()




clock = pygame.time.Clock()


cloud_image = pygame.image.load("cloud.png").convert_alpha()

person_image = pygame.image.load("person.png").convert_alpha()
umbrella_image = pygame.image.load("withUmbrella.png").convert_alpha()








personX = 0







class Rain:

    
    
    def __init__(self, xpos, ypos):
        
        self.xpos = xpos
        self.ypos = ypos
        self.size = random.randint(1, 15)
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        
        

    def move(self):
        self.ypos += random.randint (1, 15)

    def draw(self):
        
        pygame.draw.circle(screen, (self.r,self.g,self.b), (self.xpos , self.ypos), self.size, 0)



class Cloud:
    
    def __init__ (self, cloudX, speed):
        self.cloudX = cloudX
        self.y = 200
        self.speed = speed
        self.cloudDir = True

    def draw (self):
        screen.blit(cloud_image, (self.cloudX, 0))

    def dir (self):
        if self.cloudX < 0:
            self.cloudDir = True

        if self.cloudX > 1060:
            self.cloudDir = False

    def move (self):

        if self.cloudDir == True:

            self.cloudX += self.speed

        elif self.cloudDir == False:

            self.cloudX -= self.speed

    def rain(self):
        drop.append(Rain(random.randint (self.cloudX, self.cloudX + 220), self.y))



class Person:

    def __init__ (self):
        self.x = 0
        self.y = 528
       

    def draw (self):
        screen.blit (person_image, (self.x, self.y))

    def umbrella (self):
        screen.blit (umbrella_image, (self.x, self.y))

    def hit (self):
        return pygame.Rect(self.x, self.y, 170, 192) .collidepoint((drop[i].xpos, drop[i].ypos)) 

    

    
        

lastDrop = 0    
        
        
        
        
drop = []

clouds = []

for i in range(3):
    clouds.append(Cloud(random.randint(0, 1060), random.randint(1, 5)))


person = Person()







  


while 1:

        

    screen.fill((80,80,80))

    clock.tick(100)

    
    for i in clouds:
        i.draw()
        i.dir()
        i.move()
        i.rain()



    


    


    ##Person
    pressed_key = pygame.key.get_pressed()
    
    if pressed_key[K_RIGHT]:
        person.x += 5

    elif pressed_key[K_LEFT]:
        person.x -= 5

    if person.x <= 0:
        person.x = 0

    elif person.x >= 980:
        person.x = 980

    
    
    
    
    
    

    

    

        
            

    
    
    i = 0
    while i < len(drop):
        drop[i].move()

        drop[i].draw()

        if person.hit():
            lastDrop = time.time()
            
        
        if drop[i].ypos > 680 or person.hit():
            del drop[i]
            i -= 1

        

            
            

        i += 1

        

        
            


    if time.time() - lastDrop > 1:
        person.draw()
    else:
        person.umbrella()

    
        



    

   
            
        
            

       
            


    
            
            
            







    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit


    pygame.display.update()

    
