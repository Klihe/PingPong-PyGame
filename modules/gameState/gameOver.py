# end.py
import pygame
from modules.colors import Color

# draw items in GAME_OVER - state
def drawGameOver(win, windowWidth, windowHeight) -> None:
    win.fill(Color.BLACK)
    gameOverFont = pygame.font.Font(None, 36)
    # pygame.draw.rect(win, Color.WHITE, (960 - 650, 540 - 250, 500, 500))
    # pygame.draw.rect(win, Color.WHITE, (960 + 150, 540 - 250, 500, 500))
    # pygame.draw.circle(win, Color.WHITE, (960, 540), 20)
    text = gameOverFont.render("Game Over", True, Color.WHITE)
    win.blit(text, (windowWidth // 2 - text.get_width() // 2, windowHeight // 2 - text.get_height() // 2))