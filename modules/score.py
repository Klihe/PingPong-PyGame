# score.py
import pygame
from modules.config import Config
from modules.colors import Color

def renderScores(win, font, players) -> None:
    scoreText1 = font.render("Score: " + str(players[0].score), True, Color.WHITE)
    win.blit(scoreText1, (100, 18))

    scoreText2 = font.render("Score: " + str(players[1].score), True, Color.WHITE)
    win.blit(scoreText2, (Config.WINDOW_WIDTH - 200, 18))

# def renderAbilityIndicators(win, players):
#     pygame.draw.circle(win, players[0].abilities[0].active(), (30 + 15, Config.WINDOW_HEIGHT // 2), 15)
#     pygame.draw.circle(win, players[1].abilities[0], (Config.WINDOW_WIDTH - 30 - 15, Config.WINDOW_HEIGHT // 2), 15)
#     pygame.draw.circle(win, players[0].abilities[1], (30 + 20 + 15 + 20, Config.WINDOW_HEIGHT // 2), 15)
#     pygame.draw.circle(win, players[1].abilities[1], (Config.WINDOW_WIDTH - 30 - 20 - 15 - 20, Config.WINDOW_HEIGHT // 2), 15)