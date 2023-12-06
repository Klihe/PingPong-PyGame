# menu.py
import pygame
from modules.colors import Color

# draw item in MENU - state
def drawMenu(win, window_width, window_height) -> None:
    menu_font = pygame.font.Font(None, 48)
    # text = menu_font.render("Press SPACE to Start", True, Color.WHITE)
    pygame.draw.rect(win, Color.WHITE, (60, 60, 870, 960))
    pygame.draw.rect(win, Color.BLACK, (90, 90, 810, 120))
    pygame.draw.rect(win, Color.BLACK, (90, 240, 810 / 2 - 15, 750))
    pygame.draw.rect(win, Color.BLACK, (510, 240, 810 / 2 - 15, 750 / 2 - 15))
    pygame.draw.rect(win, Color.BLACK, (510, 630, 810 / 2 - 15, 750 / 2 - 15))
    pygame.draw.rect(win, Color.WHITE, (990, 60, 870, 960))
    win.blit(text, (window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2))