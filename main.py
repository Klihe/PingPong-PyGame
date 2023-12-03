import pygame
from modules.game import Game

# Initialize Pygame
pygame.init()

# Set up game window
win_width = 1920
win_height = 1080
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Your Game Title")

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
    win.fill((0, 0, 0))  # Fill the window with black background
    game.draw(win)

    # Update the display
    pygame.display.flip()

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()