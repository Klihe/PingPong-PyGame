# main.py
import pygame
from modules.game import Game
from modules.config import Config
from modules.colors import Color

# Initialize Pygame
pygame.init()

# Set up game window
winMain = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
pygame.display.set_caption("PingPong")

# Create game instance
game = Game()

# Main game loop
clock = pygame.time.Clock()
running = True
pause = False

while running:
    clock.tick(60)  # Set the frame rate
    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause = not pause
    
    if not pause:
        # Handle events
        game.handleEvents()
        # Update game state
        game.update()
        # Draw the game
        game.draw(winMain)

        # Update the display
        pygame.display.flip()

# Quit Pygame
pygame.quit()