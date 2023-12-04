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

        self.keyUp = keyUp
        self.keyDown = keyDown
        self.speed = speed
        self.color = color
        self.score = 0

        self.abilities = []
        self.adjustedY = False

    def movement(self, keys):
        if keys[self.keyUp] and self.y > 0:
            self.y -= self.speed
        if keys[self.keyDown] and self.y < Config.WINDOW_HEIGHT - self.height:
            self.y += self.speed

    def update(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        for ability in self.abilities:
            ability.update()
    
    def increaseScore(self):
        self.score += 1