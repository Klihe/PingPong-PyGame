import pygame

from modules.config import Config
from modules.game import Game

window_main = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
pygame.display.set_caption("PingPong")

game = Game()

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game.event()
    game.update(pygame.time.get_ticks(), pygame.key.get_pressed())
    game.draw(window_main)

pygame.init()