import pygame

class Ability:
    def __init__(self, button, cooldown, duration, startFunc = lambda: None, endFunc = lambda: None, updateFunc = lambda: None):
        self.button = button
        self.cooldown = cooldown
        self.duration = duration

        self.startFunc = startFunc
        self.endFunc = endFunc
        self.updateFunc = updateFunc

        self.lastUse = 0
        self.active = False

    def startFunc(self) -> None:
        if self.cooldown > pygame.time.get_ticks - self.lastUse:
            return
        self.lastUse = pygame.time.get_ticks

    def endFunc(self) -> None:
        self.active = False

    def updateFunc(self) -> None:
        if self.duration > pygame.time.get_ticks() - self.lastUse:
            self.endFunc()
            return