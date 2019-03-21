import pygame, random

black = (  0,   0,   0)
white = (255, 255, 255)
red = (255,   0,   0)

class Collectible(pygame.sprite.Sprite):

    def __init__ (self, colour, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode([screen_width, screen_height])

collectibleList = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

score = 0
clock = pygame.time.Clock()


for i in  range(50):
    collectible = Collectible(black, 20, 15)

    collectible.rect.x = random.randrange(screen_width - 20)
    collectible.rect.y = random.randrange(screen_height - 15)

    collectibleList.add(collectible)
    all_sprite_list.add(collectible)

    #Player
    player = Collectible(red, 10, 20)
    all_sprite_list.add(player)

done = False


while done == False:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    screen.fill(white)
    
    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    collectibleHitList = pygame.sprite.spritecollide(player, collectibleList, True)

    for collectible in collectibleHitList:
        score += 1
        print(score)

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
        




    
    
