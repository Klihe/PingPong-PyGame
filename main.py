# Libraries
import pygame
import random
import math

# init pygame
pygame.init()

# Settings
winWidth = 1920
winHeight = 1080

# Config
pygame.display.set_caption("Ping Pong")
winMain = pygame.display.set_mode((winWidth, winHeight))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Const variables

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (204, 49, 61)
BLUE = (64, 142, 198)
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
        self.score = 0
        self.abilityActive1 = False
        self.abilityLast1 = 0
        self.abilityActive2 = False
        self.abilityLast2 = 0

    # Move up,down
    def movement(self, up, down):
        if keys[up] and self.y > 0:
            self.y -= self.speed
        if keys[down] and self.y < winHeight - self.height:
            self.y += self.speed

    # Make player bigger
    def beBigger(self, slot, cooldownTime, abilityTime):
        currentTime = pygame.time.get_ticks()
        if keys[slot] and not self.abilityActive1 and currentTime - self.abilityLast1 > cooldownTime:
            self.abilityActive1 = True
            self.abilityLast1 = currentTime
        if self.abilityActive1:
            if currentTime - self.abilityLast1 < abilityTime:
                self.height = BLOCK * 4
            else:
                self.height = BLOCK * 2
                self.abilityActive1 = False

    # Make player faster
    def beFaster(self, slot, cooldownTime, abilityTime):
        currentTime = pygame.time.get_ticks()
        if keys[slot] and not self.abilityActive2 and currentTime - self.abilityLast2 > cooldownTime:
            self.abilityActive2 = True
            self.abilityLast2 = currentTime
        if self.abilityActive2:
            if currentTime - self.abilityLast2 < abilityTime:
                self.speed = 20
            else:
                self.speed = 10
                self.abilityActive2 = False

    # Put player to the frame
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
        self.direction = random.choice([-45, -225, 45, 225])
    
    # Movement on screen
    def movement(self):
        self.x += int(self.speed * math.cos(math.radians(self.direction)))
        self.y += int(self.speed * math.sin(math.radians(self.direction)))

        if self.y - self.radius <= 0 or self.y + self.radius >= winHeight:
            self.direction = -self.direction
        
        if self.x - self.radius <= 0:
            player2.score += 1
            self.speed = 10
            self.reset([-45, 45])
        
        elif self.x + self.radius >= winWidth:
            player1.score += 1
            self.speed = 10
            self.reset([-225, 225])
    
    # Collisions with player
    def checkCollision(self, player):
        if (
            self.x + self.radius >= player.x
            and self.x - self.radius <= player.x + player.width
            and self.y + self.radius >= player.y
            and self.y - self.radius <= player.y + player.height
        ):
            self.direction = 180 - self.direction
            self.speed += 1
    
    # Reset position
    def reset(self, direction):
        self.x = winWidth // 2
        self.y = winHeight // 2
        self.direction = random.choice(direction)

    # Put ball to the frame
    def update(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# Update Frame
def winUpdate():
    winMain.fill(BLACK)
    # Class
    player1.update(winMain)
    player2.update(winMain)
    ball.update(winMain)
    # Text
    score_text1 = font.render("Score: " + str(player1.score), True, WHITE)
    score_text2 = font.render("Score: " + str(player2.score), True, WHITE)
    winMain.blit(score_text1, (20, 20))
    winMain.blit(score_text2, (winWidth - 150, 20))
    # Update
    pygame.display.update()

# Create objects
player1 = Player(BLOCK / 2, winHeight / 2, BLOCK / 2, BLOCK * 2, 10, RED)
player2 = Player(winWidth - BLOCK / 2 - BLOCK / 2, winHeight / 2, BLOCK / 2, BLOCK * 2, 10, BLUE)
ball = Ball(winWidth / 2, winHeight / 2, BLOCK / 4, 10, WHITE)

# Game
run = True
while run:
    clock.tick(60)

    # Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Pressed buttons
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
            game_display = pygame.display.set_mode((winWidth, winHeight))

    # Movement
    player1.movement(pygame.K_w, pygame.K_s)
    player2.movement(pygame.K_UP, pygame.K_DOWN)
    ball.movement()

    # Abilities of players
    player1.beBigger(pygame.K_a, 10000, 2500)
    player2.beBigger(pygame.K_LEFT, 10000, 2500)
    player1.beFaster(pygame.K_d, 5000, 2500)
    player2.beFaster(pygame.K_RIGHT, 5000, 2500)

    # Collision between ball and players
    ball.checkCollision(player1)
    ball.checkCollision(player2)

    # Update frame
    winUpdate()
    
# If run = False
pygame.quit()