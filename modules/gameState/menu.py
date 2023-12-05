# menu.py
import pygame
from modules.colors import Color

def drawMenu(win, window_width, window_height):
    menu_font = pygame.font.Font(None, 48)
    text = menu_font.render("Press SPACE to Start", True, Color.WHITE)
    win.blit(text, (window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2))