# ability.py
import pygame

class Ability:
    def __init__(self, player, cooldownTime, abilityTime):
        self.player = player
        self.cooldownTime = cooldownTime
        self.abilityTime = abilityTime
        self.lastUse = 0
        self.active = False

    def startFunc(self) -> None:
        if self.cooldownTime > pygame.time.get_ticks() - self.lastUse:
            return
        self.lastUse = pygame.time.get_ticks()
        self.active = True
        
    def endFunc(self) -> None:
        if self.active:
            self.lastUse = pygame.time.get_ticks()
        self.active = False

    def updateFunc(self) -> None:
        if self.abilityTime < pygame.time.get_ticks() - self.lastUse:
            self.endFunc()