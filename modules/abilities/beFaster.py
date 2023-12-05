# beFaster.py
from modules.abilities.ability import Ability

class BeFaster(Ability):
    def __init__(self, player, cooldownTime, abilityTime, speedIncrease):
        super().__init__(player, cooldownTime, abilityTime)
        self.speedIncrease = speedIncrease

    def startFunc(self):
        super().startFunc()
        if self.active:
            self.player.speed = self.speedIncrease

    def endFunc(self):
        super().endFunc()
        self.player.speed = self.speedIncrease / 2