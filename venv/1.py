import pygame
pygame.init()
windowX = 1000
windowY = 480;
window = pygame.display.set_mode((windowX,windowY))

pygame.display.set_caption("FIrst game")

run = True


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('mybg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()
class player():
    def __init__(self , x , y , width , height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.IsJump = False
        self.jumpm = -10
        self.jumpp = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self , window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(char, (self.x, self.y))
def redrawGameWindow():


    window.blit(bg, (0 , 0))
    man.draw(window)
    pygame.display.update()
man = player(50, 400, 64 , 64)
woman = player(200, 400, 64 , 64)
while run:
    clock.tick(27)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed();
    if keys[pygame.K_RIGHT] and man.x < windowX - man.width - man.speed:
        man.x+=man.speed
        man.right = True
        man.left = False
    elif keys[pygame.K_LEFT] and man.x > man.speed:
        man.x-=man.speed
        man.left = True
        man.right = False
    else:
        man.left = False
        man.right = False
        man.walkCount = 0
    if man.IsJump == False:
        if keys[pygame.K_SPACE]:
            man.IsJump = True
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpm <= man.jumpp:
            if man.jumpm >= 0:
                man.y += man.jumpm*man.jumpm / 2
            else: man.y -= man.jumpm*man.jumpm / 2
            man.jumpm += 1
        else:
            man.IsJump = False
            man.jumpm = -10
            man.jumpp = 10


    redrawGameWindow()


pygame.QUIT
