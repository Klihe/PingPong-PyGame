import pygame
from colors import Color
from config import Config

class Player():
    def __init__(self, x, y, width, height, keyUp, keyDown, speed, color, ability1, ability2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.keyUp = keyUp
        self.keyDown = keyDown
        self.speed = speed
        self.color = color
        self.ability1 = ability1
        self.ability2 = ability2

        self.abilityActive = None
        self.score = 0

    # Move up,down
    def movement(self, keys):
        if keys[self.keyUp] and self.y > 0:
            self.y -= self.speed
        if keys[self.keyDown] and self.y < Config.winHeight - self.height:
            self.y += self.speed

    def render(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if self.ability1.active:
            pygame.draw.circle(win)
        else:
            pygame.draw.circle(win)

    # Put player to the frame
    def update(self):
        if self.abilityActive:
            self.abilityActive.update()
