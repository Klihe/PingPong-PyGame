import pygame
from modules.game import Game
from modules.config import Config
from modules.colors import Color
from modules.objects.ball import Ball
from modules.objects.player import Player

# Initialize Pygame
pygame.init()

# Set up game window
win = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
pygame.display.set_caption("PingPong")

# Create game instance
game = Game()

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # Set the frame rate
    
    # Handle events
    game.handleEvents()

    # Update game state
    game.update(win)

    # Draw the game
    win.fill((Color.BLACK))  # Fill the window with black background
    game.draw(win)

    # Update the display
    pygame.display.flip()

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()