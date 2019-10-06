import pygame
pygame.init()
windowX = 1000
windowY = 480;
window = pygame.display.set_mode((windowX,windowY))

pygame.display.set_caption("FIrst game")

run = True


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkEnemyRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load("R11E.png")]
walkEnemyLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png') , pygame.image.load("L11E.png")]

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
        self.standing  = False
    def draw(self , window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                if self == enemy:
                    window.blit(walkEnemyLeft[self.walkCount// 3], (self.x, self.y))
                else:
                    window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                if self == enemy:
                    window.blit(walkEnemyRight[self.walkCount // 3], (self.x, self.y))
                else:
                    window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self == enemy:
                if self.right:
                    window.blit(walkEnemyRight[0] , (self.x, self.y))
                elif self.left:
                    window.blit(walkEnemyLeft[0], (self.x, self.y))
            else:
                if self.right:
                    window.blit(walkRight[0] , (self.x, self.y))
                elif self.left:
                    window.blit(walkLeft[0], (self.x, self.y))
                else:
                    window.blit(char, (self.x , self.y))
class projectile():
    def __init__(self, x , y , radius , color , facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing
    def draw(self,window):
        pygame.draw.circle(window ,self.color ,  (self.x , self.y) , self.radius)


def redrawGameWindow():
    window.blit(bg, (0 , 0))
    man.draw(window)
    woman.draw(window)
    enemy.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()

man = player(50, 400, 64 , 64)
woman = player(200, 400, 64 , 64)
enemy = player(600, 400, 64, 64)
bullets = []
manControl = True
womanControl = False

while run:
    clock.tick(27)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    keys = pygame.key.get_pressed();
    if keys[pygame.K_v]:
        if man.left:
            facing = -1
        if man.right:
            facing = 1
        bullets.append(projectile(int(man.x), int(man.y), 10, (0, 0, 0), facing))

    for bullet in bullets:
        bullet.x += bullet.speed
        if (bullet.x == enemy.x and enemy.x < windowX - enemy.width - enemy.speed) or ( bullet.x >= enemy.x and bullet.x <= enemy.x + enemy.width and enemy.x < windowX - enemy.width - enemy.speed):
            enemy.x += bullet.speed


    if keys[pygame.K_1]:
        manControl = True
        womanControl = False
    elif keys[pygame.K_2]:
        manControl = False
        womanControl = True

    if manControl:
        if keys[pygame.K_RIGHT] and man.x < windowX - man.width - man.speed:
            man.x+=man.speed
            man.right = True
            man.left = False
            man.standing = False
        elif keys[pygame.K_LEFT] and man.x > man.speed:
            man.x-=man.speed
            man.left = True
            man.right = False
            man.standing = False
        else:
            man.standing = True
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
    elif womanControl:
        if keys[pygame.K_RIGHT] and woman.x < windowX - woman.width - woman.speed:
            woman.x+=woman.speed
            woman.right = True
            woman.left = False
            woman.standing = False
        elif keys[pygame.K_LEFT] and woman.x > woman.speed:
            woman.x-=woman.speed
            woman.left = True
            woman.right = False
            woman.standing = False
        else:
            woman.standing = True
            woman.walkCount = 0
        if woman.IsJump == False:
            if keys[pygame.K_SPACE]:
                woman.IsJump = True
                woman.left = False
                woman.right = False
                woman.walkCount = 0
        else:
            if woman.jumpm <= woman.jumpp:
                if woman.jumpm >= 0:
                    woman.y += woman.jumpm*woman.jumpm / 2
                else: woman.y -= woman.jumpm*woman.jumpm / 2
                woman.jumpm += 1
            else:
                woman.IsJump = False
                woman.jumpm = -10
                woman.jumpp = 10

    if keys[pygame.K_d] and enemy.x < windowX - enemy.width - enemy.speed:
        enemy.x+=enemy.speed
        enemy.right = True
        enemy.left = False
        enemy.standing = False
    elif keys[pygame.K_a] and enemy.x > enemy.speed:
        enemy.x-=enemy.speed
        enemy.left = True
        enemy.right = False
        enemy.standing = False
    else:
        enemy.standing = True
        enemy.walkCount = 0
    if enemy.IsJump == False:
        if keys[pygame.K_w]:
            enemy.IsJump = True
            enemy.left = False
            enemy.right = False
            enemy.walkCount = 0
    else:
        if enemy.jumpm <= enemy.jumpp:
            if enemy.jumpm >= 0:
                enemy.y += enemy.jumpm*enemy.jumpm / 2
            else: enemy.y -= enemy.jumpm*enemy.jumpm / 2
            enemy.jumpm += 1
        else:
            enemy.IsJump = False
            enemy.jumpm = -10
            enemy.jumpp = 10

    redrawGameWindow()


pygame.QUIT
