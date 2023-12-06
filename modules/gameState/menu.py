# menu.py
import pygame
from modules.colors import Color
from modules.objects.player import Player

# draw item in MENU - state
def drawMenu(win, windowWidth, windowHeight, players) -> None:
    menuFont = pygame.font.Font(None, 48)
    nameFont = pygame.font.Font(None, 120)
    statsFont = pygame.font.Font(None, 48)
    charFont = pygame.font.Font(None, 200)
    # Player 1
    # background
    pygame.draw.rect(win, Color.WHITE, (60, 60, 870, 960))
    # name
    pygame.draw.rect(win, Color.BLACK, (90, 90, 810, 120))
    name = nameFont.render(players[0].name, True, Color.WHITE)
    win.blit(name, (100, 110))
    # character
    pygame.draw.rect(win, Color.BLACK, (90, 240, 810 / 2 - 15, 750))
    pygame.draw.rect(win, players[0].color, (225, 380, 120, 480))
    # char = charFont.render("" + str(players[0].value), True, Color.WHITE)
    # win.blit(char, (120, 400))
    # stats
    pygame.draw.rect(win, Color.BLACK, (510, 240, 810 / 2 - 15, 750 / 2 - 15))
    width = statsFont.render("Width: " + str(players[0].width), True, Color.WHITE)
    win.blit(width, (525, 255))
    height = statsFont.render("Height: " + str(players[0].height), True, Color.WHITE)
    win.blit(height, (525, 255 + 48 + 15))
    speed = statsFont.render("Speed: " + str(players[0].speed), True, Color.WHITE)
    win.blit(speed, (525, 255 + 96 + 30))
    # specialAbility = statsFont.render("Special Ability: " + str(players[0].score), True, Color.WHITE)
    # ability
    pygame.draw.rect(win, Color.BLACK, (510, 630, 810 / 2 - 15, 750 / 2 - 15))

    # Player 2
    # background
    pygame.draw.rect(win, Color.WHITE, (990, 60, 870, 960))
    # name
    pygame.draw.rect(win, Color.BLACK, (90 + 930, 90, 810, 120))
    name = nameFont.render(players[1].name, True, Color.WHITE)
    win.blit(name, (100 + 930, 110))
    # character
    pygame.draw.rect(win, Color.BLACK, (90 + 930, 240, 810 / 2 - 15, 750))
    pygame.draw.rect(win, players[1].color, (225 + 930, 380, 120, 480))
    # char = charFont.render("" + str(players[0].value), True, Color.WHITE)
    # win.blit(char, (120, 400))
    # stats
    pygame.draw.rect(win, Color.BLACK, (510 + 930, 240, 810 / 2 - 15, 750 / 2 - 15))
    width = statsFont.render("Width: " + str(players[1].width), True, Color.WHITE)
    win.blit(width, (525 + 930, 255))
    height = statsFont.render("Height: " + str(players[1].height), True, Color.WHITE)
    win.blit(height, (525 + 930, 255 + 48 + 15))
    speed = statsFont.render("Speed: " + str(players[1].speed), True, Color.WHITE)
    win.blit(speed, (525 + 930, 255 + 96 + 30))
    # specialAbility = statsFont.render("Special Ability: " + str(players[0].score), True, Color.WHITE)
    # ability
    pygame.draw.rect(win, Color.BLACK, (510 + 930, 630, 810 / 2 - 15, 750 / 2 - 15))