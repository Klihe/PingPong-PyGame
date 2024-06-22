# game.py
import pygame
from modules.config import Config
from modules.colors import Color
from modules.score import renderScores
from modules.objects.player import Player
from modules.objects.ball import Ball
from modules.abilities.beTaller import BeTaller
from modules.abilities.beFaster import BeFaster
from modules.gameState.menu import drawMenu
from modules.gameState.gameOver import drawGameOver
from modules.gameState.state import GameState
from modules.character import characterValue

class Game:
    def __init__(self):
        # implement menu system
        self.state = GameState.MENU

        # create players
        self.players = [
            Player(value=0, x=30, y=Config.WINDOW_HEIGHT / 2, keyUp=pygame.K_w, keyDown=pygame.K_s, color=Color.RED),
            Player(value=0, x=Config.WINDOW_WIDTH - 60, y=Config.WINDOW_HEIGHT / 2, keyUp=pygame.K_UP, keyDown=pygame.K_DOWN, color=Color.BLUE)
        ]


        # give them abilities
        self.players[0].addAbility(BeTaller(player=self.players[0]))
        self.players[1].addAbility(BeTaller(player=self.players[0]))
        self.players[0].addAbility(BeFaster(player=self.players[1]))
        self.players[1].addAbility(BeFaster(player=self.players[1]))

        # create ball
        self.ball = Ball(x=Config.WINDOW_WIDTH // 2, y=Config.WINDOW_HEIGHT // 2, radius=15, speed=10, color=Color.WHITE)
        # basic font
        self.font = pygame.font.Font(None, 36)
    
    def handleEvents(self) -> None:
        # takes pressed keys
        keys = pygame.key.get_pressed()

        # MENU - state
        if self.state == GameState.MENU:
            if keys[pygame.K_a]:
                self.players[0].plusValue(-1, len(characterValue) - 1)
            if keys[pygame.K_d]:
                self.players[0].plusValue(1, len(characterValue) - 1)       
            # activate abilities for player2
            if keys[pygame.K_LEFT]:
                self.players[1].plusValue(-1, len(characterValue) - 1)
            if keys[pygame.K_RIGHT]:
                self.players[1].plusValue(1, len(characterValue) - 1)

            if keys[pygame.K_SPACE]:
                self.state = GameState.PLAYING

        # PLAYING - state
        elif self.state == GameState.PLAYING:

            # Check for quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # activate abilities for player1
            if keys[pygame.K_a]:
                self.players[0].abilities[0].startFunc()
            if keys[pygame.K_d]:
                self.players[0].abilities[1].startFunc()
            if keys[pygame.K_LEFT]:
                self.players[1].abilities[0].startFunc()
            if keys[pygame.K_RIGHT]:
                self.players[1].abilities[1].startFunc()
            
            # GAME OVER - when someone has 25 score
            for player in self.players:
                    if player.score >= 25:
                        self.state = GameState.GAME_OVER
        
        # GAME OVER - state
        elif self.state == GameState.GAME_OVER:
            # reset game
            if keys[pygame.K_SPACE]:
                self.resetGame()
                self.state = GameState.MENU
                pygame.time.delay(100)

    def update(self) -> None:
        # MENU - state
        if self.state == GameState.MENU:
            # character selection
            for player in self.players:
                player.selectCharacter(characterValue[player.value])
                player.selectCharacter(characterValue[player.value])

        # PLAYING - state
        elif self.state == GameState.PLAYING:
            # update position of all players
            for player in self.players:
                    player.movement(pygame.key.get_pressed())

            # update state of abilities - player1
            for player in self.players:
                for ability in player.abilities:
                    ability.updateFunc()

            # player1 - boarder
            if self.ball.x - self.ball.radius <= 0:
                self.players[1].increaseScore()
                self.ball.speed = self.ball.originalSpeed
                self.ball.reset([-45, 45])
            # player2 - boarder
            elif self.ball.x + self.ball.radius >= Config.WINDOW_WIDTH:
                self.players[0].increaseScore()
                self.ball.speed = self.ball.originalSpeed
                self.ball.reset([-225, 225])

            # update position of ball
            self.ball.movement()
            # check collision behind players and ball
            for player in self.players:
                self.ball.checkCollision(player)

    def draw(self, win) -> None:
        # MENU - state
        if self.state == GameState.MENU:
            # draw menu
            drawMenu(win, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT, self.players)

        # PLAYING - state
        elif self.state == GameState.PLAYING:
            # draw everything on mainWin
            win.fill(Color.BLACK)
            for player in self.players:
                player.draw(win)
            self.ball.draw(win)
            renderScores(win, self.font, self.players)

        # GAME OVER - state
        elif self.state == GameState.GAME_OVER:
            drawGameOver(win, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)

    # restart game
    def resetGame(self) -> None:
        self.state = GameState.PLAYING
        for player in self.players:
            player.score = 0