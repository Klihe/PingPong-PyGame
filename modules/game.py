# game.py
import pygame
from modules.config import Config
from modules.colors import Color
from modules.score import renderScores
from modules.objects.player import Player
from modules.objects.ball import Ball
from modules.abilities.beBigger import BeBigger
from modules.abilities.beFaster import BeFaster
from modules.gameState.menu import drawMenu
from modules.gameState.gameOver import drawGameOver
from modules.gameState.state import GameState

class Game:
    def __init__(self):
        self.state = GameState.MENU
        self.players = [
            Player(x=30, y=Config.WINDOW_HEIGHT / 2, width=30, height=120, keyUp=pygame.K_w, keyDown=pygame.K_s, speed=10, color=Color.RED),
            Player(x=Config.WINDOW_WIDTH - 60, y=Config.WINDOW_HEIGHT / 2, width=30, height=120, keyUp=pygame.K_UP, keyDown=pygame.K_DOWN, speed=10, color=Color.BLUE)
        ]

        self.abilitiesPlayer1 = [
            BeBigger(player=self.players[0], cooldownTime=2000, abilityTime=5000),
            BeFaster(player=self.players[0], cooldownTime=3000, abilityTime=4000, speedIncrease=20)
        ]
        self.abilitiesPlayer2 = [
            BeBigger(player=self.players[1], cooldownTime=2000, abilityTime=5000),
            BeFaster(player=self.players[1], cooldownTime=3000, abilityTime=4000, speedIncrease=20)
        ]

        self.ball = Ball(x=Config.WINDOW_WIDTH // 2, y=Config.WINDOW_HEIGHT // 2, radius=15, speed=10, color=Color.WHITE)
        self.font = pygame.font.Font(None, 36)
    
    def handleEvents(self) -> None:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.state == GameState.MENU:   
            if keys[pygame.K_SPACE]:
                self.state = GameState.PLAYING
        elif self.state == GameState.PLAYING:

            if keys[pygame.K_a]:
                self.abilitiesPlayer1[0].startFunc()
            if keys[pygame.K_d]:
                self.abilitiesPlayer1[1].startFunc()
            
            if keys[pygame.K_LEFT]:
                self.abilitiesPlayer2[0].startFunc()
            if keys[pygame.K_RIGHT]:
                self.abilitiesPlayer2[1].startFunc()
            
            for player in self.players:
                    if player.score >= 25:
                        self.state = GameState.GAME_OVER
        
        elif self.state == GameState.GAME_OVER:
            if keys[pygame.K_SPACE]:
                self.reset_game()
                self.state = GameState.MENU

    def update(self) -> None:
        if self.state == GameState.PLAYING:
            for player in self.players:
                    player.movement(pygame.key.get_pressed())
                    player.update()

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

    def draw(self, win) -> None:
        if self.state == GameState.MENU:
            drawMenu(win, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)

        elif self.state == GameState.PLAYING:
            for player in self.players:
                player.draw(win)
            self.ball.update(win)
            renderScores(win, self.font, self.players)

        elif self.state == GameState.GAME_OVER:
            drawGameOver(win, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)

    def reset_game(self) -> None:
        self.state = GameState.PLAYING
        for player in self.players:
            player.score = 0