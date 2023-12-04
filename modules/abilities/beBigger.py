# beBigger.py
from modules.abilities.ability import Ability

class BeBigger(Ability):
    def __init__(self, player, slot, cooldownTime, abilityTime):
        super().__init__(player, cooldownTime, abilityTime)
        self.slot = slot

    def startFunc(self):
        super().startFunc()
        if self.active:
            self.player.height = self.player.originalHeight * 2
            if not self.player.adjustedY:
                self.player.y -= self.player.originalHeight / 2
                self.player.adjustedY = True

    def endFunc(self):
        super().endFunc()
        self.player.height = self.player.originalHeight
        if self.player.adjustedY:
                self.player.y += self.player.originalHeight / 2
                self.player.adjustedY = False

    def updateFunc(self):
        super().updateFunc()