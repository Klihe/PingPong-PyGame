# player.py
import pygame
from modules.config import Config

class Player:
    def __init__(self, x, y, width, height, keyUp, keyDown, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.originalHeight = height
        self.speed = speed

        self.keyUp = keyUp
        self.keyDown = keyDown
        self.color = color
        self.score = 0

        self.adjustedY = False

    # Movement of player
    def movement(self, keys) -> None:
        # Up
        if keys[self.keyUp] and self.y > 0:
            self.y -= self.speed
        # Down
        if keys[self.keyDown] and self.y < Config.WINDOW_HEIGHT - self.height:
            self.y += self.speed

    # Draw the player in the window
    def draw(self, win) -> None:
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    # Increase the score for the player
    def increaseScore(self) -> None:
        self.score += 1