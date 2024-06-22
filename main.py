# main.py
import pygame
from modules.game import Game
from modules.gameState.state import GameState
from modules.config import Config

# Initialize Pygame
pygame.init()

# Set up game window
winMain = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT), pygame.FULLSCREEN)
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
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and game.state == GameState.PLAYING:
            if event.key == pygame.K_SPACE:
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