# game.py
import pygame
from modules.config import Config
from modules.colors import Color
from modules.objects.player import Player
from modules.objects.ball import Ball
from modules.abilities.beBigger import BeBigger
from modules.abilities.beFaster import BeFaster

class Game:
    def __init__(self):
        self.players = [
            Player(x=30, y=Config.WINDOW_HEIGHT / 2, width=30, height=120, keyUp=pygame.K_w, keyDown=pygame.K_s, speed=10, color=Color.RED),
            Player(x=Config.WINDOW_WIDTH - 60, y=Config.WINDOW_HEIGHT / 2, width=30, height=120, keyUp=pygame.K_UP, keyDown=pygame.K_DOWN, speed=10, color=Color.BLUE)
        ]

        self.abilitiesPlayer1 = [
            BeBigger(player=self.players[0], slot=0, cooldownTime=2000, abilityTime=5000),
            BeFaster(player=self.players[0], slot=1, cooldownTime=3000, abilityTime=4000, speedIncrease=20)
        ]
        self.abilitiesPlayer2 = [
            BeBigger(player=self.players[1], slot=0, cooldownTime=2000, abilityTime=5000),
            BeFaster(player=self.players[1], slot=1, cooldownTime=3000, abilityTime=4000, speedIncrease=20)
        ]

        self.ball = Ball(x=Config.WINDOW_WIDTH // 2, y=Config.WINDOW_HEIGHT // 2, radius=15, speed=10, color=Color.WHITE)
    
    def handleEvents(self):
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if keys[pygame.K_a]:
            self.abilitiesPlayer1[0].startFunc()
        if keys[pygame.K_d]:
            self.abilitiesPlayer1[1].startFunc()
        
        if keys[pygame.K_LEFT]:
            self.abilitiesPlayer2[0].startFunc()
        if keys[pygame.K_RIGHT]:
            self.abilitiesPlayer2[1].startFunc()

    def update(self, win):
        for player in self.players:
            player.movement(pygame.key.get_pressed())
            player.update(win)

        for ability in self.abilitiesPlayer1:
            ability.updateFunc()

        for ability in self.abilitiesPlayer2:
            ability.updateFunc()

        if self.ball.x - self.ball.radius <= 0:
            self.players[1].increaseScore()
            self.ball.speed = 10
            self.ball.reset([-45, 45])

        elif self.ball.x + self.ball.radius >= Config.WINDOW_WIDTH:
            self.players[0].increaseScore()
            self.ball.speed = 10
            self.ball.reset([-225, 225])

        self.ball.movement()
        for player in self.players:
            self.ball.checkCollision(player)

    def draw(self, win):
        for player in self.players:
            player.update(win)

        self.ball.update(win)