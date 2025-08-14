import pygame
pygame.init()
#set dimensions of the screen
screen = pygame.display.set_mode((1000,1000))
class Bin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("BIn.png")
        self.image = pygame.transform.scale(self.image,(100,150))
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
bin = Bin(300,300)
bingroup = pygame.sprite.Group()
bingroup.add(bin)
class Nonrecycle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Plastic Bag.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
run = True
while run:
    screen.fill("Blue")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            bin.rect.center = x,y
    bingroup.draw(screen)
    pygame.display.update()
