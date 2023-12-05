# end.py
import pygame
from modules.colors import Color

# draw items in GAME_OVER - state
def drawGameOver(win, windowWidth, windowHeight) -> None:
    gameOverFont = pygame.font.Font(None, 36)
    text = gameOverFont.render("Game Over - Press SPACE to Restart", True, Color.WHITE)
    win.blit(text, (windowWidth // 2 - text.get_width() // 2, windowHeight // 2 - text.get_height() // 2))