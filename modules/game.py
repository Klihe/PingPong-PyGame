# Score
        # Add number of bounces !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if self.x - self.radius <= 0:
            player2.score += 1
            self.speed = 10
            self.reset([-45, 45])
        
        elif self.x + self.radius >= winWidth:
            player1.score += 1
            self.speed = 10
            self.reset([-225, 225])