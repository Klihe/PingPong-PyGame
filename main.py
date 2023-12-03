# Libraries
import pygame
import random
import math
from modules.config import Config
from modules.colors import Color
from modules.gameObjects.player import Player
from modules.gameObjects.ball import Ball

# init pygame
pygame.init()

# Config
pygame.display.set_caption("Ping Pong")
winMain = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
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
    winMain.blit(scoreText2, (Config.WINDOW_WIDTH - 200, 18))
    pygame.draw.circle(winMain, player1.abilityAvailable1, (60/ 4 + 15, 60 / 2), 60 / 4)
    pygame.draw.circle(winMain, player2.abilityAvailable1, (Config.WINDOW_WIDTH - 60 / 4 - 15, 60 / 2), 60 / 4)
    pygame.draw.circle(winMain, player1.abilityAvailable2, (60 / 4 + 60 / 4 + 15 + 20, 60 / 2), 60 / 4)
    pygame.draw.circle(winMain, player2.abilityAvailable2, (Config.WINDOW_WIDTH - 60 / 4 - 60 / 4 - 15 - 20, 60 / 2), 60 / 4)

    # Update
    pygame.display.update()

# Create objects
player1 = Player(60 / 2, Config.WINDOW_HEIGHT / 2, 60 / 2, 60 * 2, pygame.K_w, pygame.K_s, 10, Color.RED)
player2 = Player(Config.WINDOW_WIDTH - 60 / 2 - 60 / 2, Config.WINDOW_HEIGHT / 2, 60 / 2, 60 * 2, pygame.K_UP, pygame.K_DOWN, 10, Color.BLUE)
ball = Ball(Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 2, 60 / 4, 10, Color.WHITE)

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
            game_display = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))

    # Movement
    player1.movement(keys)
    player2.movement(keys)
    ball.movement()

    # Abilities of players
    # player1.beBigger(pygame.K_a, 7500, 2500)
    # player2.beBigger(pygame.K_LEFT, 7500, 2500)
    # player1.beFaster(pygame.K_d, 5000, 2500)
    # player2.beFaster(pygame.K_RIGHT, 5000, 2500)

    # Collision between ball and players
    ball.checkCollision(player1)
    ball.checkCollision(player2)

    # Update frame
    winUpdate()

# If run = False
pygame.quit()