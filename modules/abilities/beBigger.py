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
                self.player.y -= self.player.originalHeight
                self.player.adjustedY = True

    def endFunc(self):
        super().endFunc()

    def updateFunc(self):
        super().updateFunc()