import pygame
import random
import math

pygame.init()

# Settings
winWidth = 1920
winHeight = 1080

# Config
winMain = pygame.display.set_mode((winWidth, winHeight))
clock = pygame.time.Clock()

# Const variables

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Values
BLOCK = 60

# Player
class Player():
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def movement(self, up, down):
        if keys[up] and self.y > 0:
            self.y -= self.speed
        if keys[down] and self.y < winHeight - self.height:
            self.y += self.speed

    def update(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

# Ball
class Ball():
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.direction = random.choice([-45, 45])
    
    def movement(self):
        self.x += int(self.speed * math.cos(math.radians(self.direction)))
        self.y += int(self.speed * math.sin(math.radians(self.direction)))

        if self.x - self.radius <= 0 or self.x + self.radius >= winWidth:
            self.direction = 180 - self.direction

        if self.y - self.radius <= 0 or self.y + self.radius >= winHeight:
            self.direction = -self.direction

    def update(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# Update Frame
def winUpdate():
    winMain.fill(BLACK)
    player1.update(winMain)
    player2.update(winMain)
    ball.update(winMain)
    pygame.display.update()

# Create objects
player1 = Player(BLOCK, winHeight / 2, BLOCK / 2, BLOCK * 2, 10, WHITE)
player2 = Player(winWidth - BLOCK - BLOCK / 2, winHeight / 2, BLOCK / 2, BLOCK * 2, 10, WHITE)
ball = Ball(winWidth / 2, winHeight / 2, BLOCK / 2, 10, WHITE)

# Game
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
            game_display = pygame.display.set_mode((winWidth, winHeight))

    player1.movement(pygame.K_w, pygame.K_s)
    player2.movement(pygame.K_UP, pygame.K_DOWN)
    ball.movement()

    winUpdate()

pygame.quit()