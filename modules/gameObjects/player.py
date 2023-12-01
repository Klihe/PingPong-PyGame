import pygame
from config import Config

class Player:
    def __init__(self, x, y, width, height, keyUp, keyDown, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.keyUp = keyUp
        self.keyDown = keyDown
        self.speed = speed
        self.color = color
        self.score = 0

        self.abilityActive1 = False
        self.abilityLast1 = 0
        self.abilityAvailable1 = False
        self.abilityActive2 = False
        self.abilityLast2 = 0
        self.abilityAvailable2 = False

    # Move up,down
    def movement(self, keys):
        if keys[self.keyUp] and self.y > 0:
            self.y -= self.speed
        if keys[self.keyDown] and self.y < Config.WINDOW_HEIGHT - self.height:
            self.y += self.speed

    # Put player to the frame
    def update(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))