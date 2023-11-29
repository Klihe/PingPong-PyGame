import pygame

class Ability:
    def __init__(self, duration, cooldown, startFunc= lambda: None, endFunc= lambda: None, updateFunc= lambda: None):
        self.duration = duration
        self.cooldown = cooldown
        self.startFunc = startFunc
        self.endFunc = endFunc
        self.updateFunc = updateFunc

        self.startTime = 0
        self.active = False

    def startFunc(self):
        if self.cooldown > pygame.time.get_ticks() - self.startTime:
            return
        self.startTime = pygame.time.get_ticks()
    
    def endFunc(self):
        self.active = False

    def updateFunc(self):
        if self.duration > pygame.time.get_ticks() - self.startTime:
            self.endFunc()
            return