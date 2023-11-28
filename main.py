# Libraries
import pygame
import random
import math

# init pygame
pygame.init()

# Settings
winWidth = 1440
winHeight = 720

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
        self.abilityAvailable1 = False
        self.abilityActive2 = False
        self.abilityLast2 = 0
        self.abilityAvailable2 = False

    # Move up,down
    def movement(self, up, down):
        if keys[up] and self.y > 0:
            self.y -= self.speed
        if keys[down] and self.y < winHeight - self.height:
            self.y += self.speed

    # Make player bigger
    def beBigger(self, slot, cooldownTime, abilityTime):
        currentTime = pygame.time.get_ticks()
        # Available
        if currentTime - self.abilityLast1 > cooldownTime or self.abilityLast1 == 0:
            self.abilityAvailable1 = self.color # mark as available
            # Pressed key
            if keys[slot] and not self.abilityActive1:
                self.abilityActive1 = True
                self.adjustedY = False
                self.abilityLast1 = currentTime
        else:
            self.abilityAvailable1 = WHITE # mark as unavailable  
            # Active
            if self.abilityActive1:
                if currentTime - self.abilityLast1 < abilityTime:
                    self.height = BLOCK * 4
                    if not self.adjustedY:
                        self.y -= BLOCK
                        self.adjustedY = True
                # Deactivate
                else:
                    self.height = BLOCK * 2
                    self.abilityActive1 = False
                    self.abilityLast1 = currentTime    


    # Make player faster
    def beFaster(self, slot, cooldownTime, abilityTime):
        currentTime = pygame.time.get_ticks()
        # Available
        if currentTime - self.abilityLast2 > cooldownTime or self.abilityLast2 == 0:
            self.abilityAvailable2 = self.color
            # Pressed key    
            if keys[slot] and not self.abilityActive2:
                self.abilityActive2 = True
                self.abilityLast2 = currentTime
        else:
            self.abilityAvailable2 = WHITE
            # Active
            if self.abilityActive2:
                if currentTime - self.abilityLast2 < abilityTime:
                    self.speed = 20
                # Deactivate
                else:
                    self.speed = 10
                    self.abilityActive2 = False
                    self.abilityLast2 = currentTime

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

        # Bounce
        if self.y - self.radius <= 0 or self.y + self.radius >= winHeight:
            self.direction = -self.direction + random.randint(-10, 10)
        
        # Score
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
            self.direction = 180 + random.randint(-10, 10) - self.direction
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
    scoreText1 = font.render("Score: " + str(player1.score), True, WHITE)
    winMain.blit(scoreText1, (100, 18))
    scoreText2 = font.render("Score: " + str(player2.score), True, WHITE)
    winMain.blit(scoreText2, (winWidth - 200, 18))
    pygame.draw.circle(winMain, player1.abilityAvailable1, (BLOCK / 4 + 15, BLOCK / 2), BLOCK / 4)
    pygame.draw.circle(winMain, player2.abilityAvailable1, (winWidth - BLOCK / 4 - 15, BLOCK / 2), BLOCK / 4)
    pygame.draw.circle(winMain, player1.abilityAvailable2, (BLOCK / 4 + BLOCK / 4 + 15 + 20, BLOCK / 2), BLOCK / 4)
    pygame.draw.circle(winMain, player2.abilityAvailable2, (winWidth - BLOCK / 4 - BLOCK / 4 - 15 - 20, BLOCK / 2), BLOCK / 4)


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
    player1.beBigger(pygame.K_a, 7500, 2500)
    player2.beBigger(pygame.K_LEFT, 7500, 2500)
    player1.beFaster(pygame.K_d, 5000, 2500)
    player2.beFaster(pygame.K_RIGHT, 5000, 2500)

    # Collision between ball and players
    ball.checkCollision(player1)
    ball.checkCollision(player2)

    # Update frame
    winUpdate()

# If run = False
pygame.quit()