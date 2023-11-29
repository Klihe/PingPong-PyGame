import pygame
import random
import math
from config import Config

class Ball():
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.direction = random.choice([-45, -225, 45, 225])
    
    # Movement on screen
    def movement(self):
        self.x += int(self.speed * math.cos(math.radians(self.direction)))
        self.y += int(self.speed * math.sin(math.radians(self.direction)))

        # Bounce
        if self.y - self.radius <= 0 or self.y + self.radius >= Config.winHeight:
            self.direction = -self.direction + random.randint(-2, 2)
        
        # Score
        if self.x - self.radius <= 0:
            player2.score += 1
            self.speed = 10
            self.reset([-45, 45])
        
        elif self.x + self.radius >= Config.winWidth:
            player1.score += 1
            self.speed = 10
            self.reset([-225, 225])
    
    # Collisions with player
    def checkCollision(self, player):
        if (
            self.x + self.radius >= player.x
            and self.x - self.radius <= player.x + player.width
            and self.y + self.radius >= player.y
            and self.y - self.radius <= player.y + player.height
        ):
            self.direction = 180 + random.randint(-5, 5) - self.direction
            self.speed += 1
    
    # Reset position
    def reset(self, direction):
        self.x = Config.winWidth // 2
        self.y = Config.winHeight // 2
        self.direction = random.choice(direction)

    # Put ball to the frame
    def update(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)