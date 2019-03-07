import pygame,sys, random, time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("My first PyGame Program")
screen = pygame.display.set_mode((1280, 720))

pygame.font.init()

spaceship = pygame.image.load("spaceship.png").convert_alpha()

alien = pygame.image.load("alien.png").convert_alpha()

background = pygame.image.load("background.png").convert_alpha()

if pygame.font.get_init():
    print("yeet")
    print(pygame.font.get_fonts())




class Ship:

    def __init__ (self):
        self.x = 640
        self.y = 680

    def draw (self):
        screen.blit (spaceship, (self.x, self.y))



class Alien:

    def __init__ (self):
        self.x = random.randint(0, 1130)
        self.y = random.randint(0, 300)

    def draw (self):
        screen.blit (alien, (self.x, self.y))

    



class Missile:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def draw (self):
        pygame.draw.rect (screen, (255,255,255), Rect(self.x, self.y, 10, 20), 0)

    def move (self):
        self.y -= 10

    def hit(self):
        return pygame.Rect(self.x, self.y, 10, 20).colliderect(Rect(aliens[i].x, aliens[i].y, 150, 150))

    
        
        



ship = Ship()

missile = []

aliens = []

spawnTime = time.time() - 3

missileTime = time.time() - 0.5

clock = pygame.time.Clock()

while 1:

    

        

    screen.fill((80,80,80))
    
    screen.blit (background, (0,0))

    clock.tick(100)

    ship.draw()

    pressed_key = pygame.key.get_pressed()
    
    if pressed_key[K_RIGHT]:
        ship.x += 5

    elif pressed_key[K_LEFT]:
        ship.x -= 5

    if ship.x <= 0:
        ship.x = 0

    elif ship.x >= 1230:
        ship.x = 1230


    if pressed_key[K_DOWN]:
        ship.y += 5

    elif pressed_key[K_UP]:
        ship.y -= 5

    if ship.y <= 400:
        ship.y = 400

    elif ship.y >= 670:
        ship.y = 670



    if pressed_key[K_SPACE] and time.time() - missileTime > 0.5:
        missile.append(Missile(ship.x + 20, ship.y))

        missileTime = time.time()

    m = 0
    while m < len(missile):
        missile[m].draw()

        missile[m].move()

        if missile[m].hit:
            del missile[m]
            m -= 1


        m += 1
        
        





    if time.time() - spawnTime > 3:
        spawnTime = time.time()
        

        aliens.append(Alien())

    i = 0
    while i < len(aliens):
        aliens[i].draw()
        
        aliens[i].y += 0.5

        if aliens[i].x < ship.x:
            aliens[i].x += 1
        elif aliens[i].x > ship.x:
            aliens[i].x -= 1

        if aliens[i].y > 700:
            del aliens[i]
            i-=1

        

            
        i += 1




    



        
    
    

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit


    pygame.display.update()

    

