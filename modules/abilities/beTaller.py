# beTaller.py
from modules.abilities.ability import Ability

class BeTaller(Ability):
    def __init__(self, player, cooldownTime, abilityTime):
        super().__init__(player, cooldownTime, abilityTime)

    # make player taller
    def startFunc(self) -> None:
        super().startFunc()
        if self.active:
            self.player.height = self.player.originalHeight * 2
            if not self.player.adjustedY:
                self.player.y -= self.player.originalHeight / 2
                self.player.adjustedY = True

    # make his height normal
    def endFunc(self) -> None:
        super().endFunc()
        self.player.height = self.player.originalHeight
        if self.player.adjustedY:
                self.player.y += self.player.originalHeight / 2
                self.player.adjustedY = False