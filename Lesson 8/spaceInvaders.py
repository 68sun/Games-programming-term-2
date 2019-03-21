import pygame,sys, random, time
from pygame.locals import *

pygame.mixer.pre_init(44100, - 16, 2, 2048)



pygame.init()
pygame.display.set_caption("My first PyGame Program")
screen = pygame.display.set_mode((1280, 720))

pygame.font.init()

spaceship = pygame.image.load("spaceship.png").convert_alpha()

alien = pygame.image.load("spaceInv.jpeg")

alien.set_colorkey((255,255,255))

background = pygame.image.load("background.png").convert_alpha()

if pygame.font.get_init():
    print("yeet")
    print(pygame.font.get_fonts())


font = pygame.font.SysFont ("arial", 20)


pygame.mixer.music.load('shoot.wav')

pygame.mixer.music.load('pacman_beginning.wav')




class Ship:

    def __init__ (self):
        self.x = 640
        self.y = 680

    def draw (self):
        screen.blit (spaceship, (self.x, self.y))

    def hit(self, alien):
        return pygame.Rect(self.x, self.y, 50, 50).colliderect(alien.x, alien.y, 40, 30)


class Alien:

    def __init__ (self):
        self.x = random.randint(0, 1130)
        self.y = random.randint(0, 300)
        self.dy = 0.05
        self.rotate =  (math.pi/2)*random.random() + 3*math.pi/4)
        self.rotateX = math.sin(self.d)*12
        self.rotateY = math.cos(self.d)*12

    def draw (self):
        screen.blit (alien, (self.x, self.y))

    def hit(self, missile):
        return pygame.Rect(self.x, self.y, 40, 30).colliderect(missile.x, missile.y, 10, 20)

    



class Missile:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def draw (self):
        pygame.draw.rect (screen, (255,255,255), Rect(self.x, self.y, 10, 20), 0)

    def move (self):
        self.y -= 10

 

    
        
        



ship = Ship()

missile = []

aliens = []

spawnTime = time.time() - 3

missileTime = time.time() - 0.5

clock = pygame.time.Clock()

lives = 10

backY = 0

score = 0



sound = pygame.mixer.Sound("shoot.wav")

startSound = pygame.mixer.Sound("pacman_beginning.wav")

startSound.play()


while 1:

    

        

    screen.fill((80,80,80))
    
    screen.blit (background, (0,backY))

    screen.blit (background, (0,backY - 720))

    backY += 1

    if backY == 720:
        backY = 0

    clock.tick(100)


    screen.blit(font.render("Score: " + str(score), True, (255,255,255)), (5,5))

    if lives > 5:
        pygame.draw.rect(screen, (128, 249, 22), Rect(5, 30, lives * 20, 15), 0)

    elif lives <= 5:
        pygame.draw.rect(screen, (249, 25, 21), Rect(5, 30, lives * 20, 15), 0)
        
    
    

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

        sound.play()

        missileTime = time.time()

    m = 0
    while m < len(missile):
        missile[m].draw()

        missile[m].move()

        

       


        m += 1



    
        
        





    if time.time() - spawnTime > 3:
        spawnTime = time.time()
        

        aliens.append(Alien())

    i = 0
    while i < len(aliens):
        if aliens[i].y > 700:
            del aliens[i]
            i -= 1

        i += 1



    
        

    i = 0
    while i < len(aliens):
        aliens[i].draw()
        
        aliens[i].y += aliens[i].dy
        aliens[i].dy += 0.05

        if aliens[i].x < ship.x:
            aliens[i].x += 1
        elif aliens[i].x > ship.x:
            aliens[i].x -= 1

        
            
            

        



        j = 0
        while j < len(missile):
            if aliens[i].hit(missile[j]):
                del aliens[i]
                del missile[j]
                i -= 1
                j -= 1
                score += 10
                

                
                break
            j += 1

                
        i += 1

    i = 0
    while i < len(aliens):

        if ship.hit(aliens[i]):
            
            if lives > 1:
                del aliens[i]
                i -= 1
                lives -= 1

            else:
                sys.exit()
        i += 1 
            
        

            
        




    



        
    
    

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit


    pygame.display.update()

    

