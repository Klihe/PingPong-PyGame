# ability.py
import pygame
class Ability:
    def __init__(self, player):
        self.player = player
        self.cooldownTime = 0
        self.abilityTime = 0
        self.lastUse = 0
        self.active = False

    # activate ability
    def startFunc(self) -> None:
        if self.cooldownTime > pygame.time.get_ticks() - self.lastUse:
            return
        self.lastUse = pygame.time.get_ticks()
        self.active = True
    
    # deactivate ability
    def endFunc(self) -> None:
        if self.active:
            self.lastUse = pygame.time.get_ticks()
        self.active = False

    # update state of ability
    def updateFunc(self) -> None:
        if self.abilityTime < pygame.time.get_ticks() - self.lastUse:
            self.endFunc()