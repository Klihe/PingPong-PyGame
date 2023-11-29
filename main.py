# Libraries
import pygame
from modules.config import Config
from modules.colors import Color
from modules.objects.ball import Ball
from modules.objects.player import Player

# init pygame
pygame.init()

# Config
pygame.display.set_caption("Ping Pong")
winMain = pygame.display.set_mode((Config.winWidth, Config.winHeight))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Update Frame
def winUpdate():
    winMain.fill(Color.BLACK)

    # Class
    player1.update(winMain)
    player2.update(winMain)
    ball.update(winMain)

    # Text
    scoreText1 = font.render("Score: " + str(player1.score), True, Color.WHITE)
    winMain.blit(scoreText1, (100, 18))
    scoreText2 = font.render("Score: " + str(player2.score), True, Color.WHITE)
    winMain.blit(scoreText2, (Config.winWidth - 200, 18))
    pygame.draw.circle(winMain, player1.abilityAvailable1, (60 / 4 + 15, 60 / 2), 60 / 4)
    pygame.draw.circle(winMain, player2.abilityAvailable1, (Config.winWidth - 60 / 4 - 60 / 4 - 15 - 20, 60 / 2), 60 / 4)
    pygame.draw.circle(winMain, player1.abilityAvailable2, (60 / 4 + 60 / 4 + 15 + 20, 60 / 2), 60 / 4)
    pygame.draw.circle(winMain, player2.abilityAvailable2, (Config.winWidth - 60 / 4 - 15, 60 / 2), 60 / 4)

    # Update
    pygame.display.update()

# Create objects
player1 = Player(60 / 2, Config.winHeight / 2, 60 / 2, 60 * 2, 10, Color.RED)
player2 = Player(Config.winWidth - 60 / 2 - 60 / 2, Config.winHeight / 2, 60 / 2, 60 * 2, 10, Color.BLUE)
ball = Ball(Config.winWidth / 2, Config.winHeight / 2, 60 / 4, 10, Color.WHITE)

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

    # Movement
    player1.movement(keys)
    player2.movement(keys)
    ball.movement()
    
    # Collision between ball and players
    ball.checkCollision(player1)
    ball.checkCollision(player2)

    # Update frame
    winUpdate()

# If run = False
pygame.quit()