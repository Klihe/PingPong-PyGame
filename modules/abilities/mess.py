# Make player bigger
def beBigger(self, slot, cooldownTime, abilityTime):
    currentTime = pygame.time.get_ticks()
    # startFunc
    if currentTime - self.abilityLast1 > cooldownTime or self.abilityLast1 == 0:
        self.abilityAvailable1 = self.color # mark as available
        # active
        if keys[slot] and not self.abilityActive1:
            self.abilityActive1 = True
            self.adjustedY = False
            self.abilityLast1 = currentTime
    else:
        self.abilityAvailable1 = Color.WHITE # mark as unavailable  
        # Active
        if self.abilityActive1:
            if currentTime - self.abilityLast1 < abilityTime:
                self.height = 60 * 4
                if not self.adjustedY:
                    self.y -= 60
                    self.adjustedY = True
            # endFunc
            else:
                self.height = 60 * 2
                self.abilityActive1 = False
                self.abilityLast1 = currentTime    


# Make player faster
def beFaster(self, slot, cooldownTime, abilityTime):
    currentTime = pygame.time.get_ticks()
    # Available
    if currentTime - self.abilityLast2 > cooldownTime or self.abilityLast2 == 0:
        self.abilityAvailable2 = self.color
        # Pressed key    
        if keys[slot] and not self.abilityActive2:
            self.abilityActive2 = True
            self.abilityLast2 = currentTime
    else:
        self.abilityAvailable2 = Color.WHITE
        # Active
        if self.abilityActive2:
            if currentTime - self.abilityLast2 < abilityTime:
                self.speed = 20
            # Deactivate
            else:
                self.speed = 10
                self.abilityActive2 = False
                self.abilityLast2 = currentTime