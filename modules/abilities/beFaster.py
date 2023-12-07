# beFaster.py
from modules.abilities.ability import Ability

class BeFaster(Ability):
    def __init__(self, player):
        super().__init__(player)
        self.cooldownTime = 2000
        self.abilityTime = 5000

    # make player faster
    def startFunc(self) -> None:
        super().startFunc()
        if self.active:
            self.player.speed = self.player.originalSpeed * 2

    # set default value
    def endFunc(self) -> None:
        super().endFunc()
        self.player.speed = self.player.originalSpeed