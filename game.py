import pygame 

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Example PyGame")

x = 50
y = 425
width = 40
height = 60
speed = 5

walkRight = [pygame.image.load('./assets/right_1.png'),
pygame.image.load('./assets/right_2.png'), pygame.image.load('./assets/right_3.png'),
pygame.image.load('./assets/right_4.png'), pygame.image.load('./assets/right_5.png'),
pygame.image.load('./assets/right_6.png'),]

walkLeft = [pygame.image.load('./assets/left_1.png'),
pygame.image.load('./assets/left_2.png'), pygame.image.load('./assets/left_3.png'),
pygame.image.load('./assets/left_4.png'), pygame.image.load('./assets/left_5.png'),
pygame.image.load('./assets/left_6.png'),]

bg = pygame.image.load('./assets/bg.jpg')
playerStand = pygame.image.load('./assets/idle.png')
isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "left"


clock = pygame.time.Clock()

class sbullet():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.bspeed = 8 * facing
    def bdraw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
def draw():
    global lastMove
    global animCount
    win.blit(bg, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0
    
    if left:
        lastMove = "left"
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        lastMove = "right"
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.bdraw(win)
    pygame.display.update()
run = True
bullets = []
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.bspeed
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        if lastMove != 'right':
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(sbullet(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))
    if keys[pygame.K_LEFT] | keys[pygame.K_a] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove == "left"
    elif keys[pygame.K_RIGHT] | keys[pygame.K_d] and x < 500 - width - 5:
        lastMove == "right"
        x += speed
        right = True
        left = False
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE] | keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    draw()

pygame.quit()